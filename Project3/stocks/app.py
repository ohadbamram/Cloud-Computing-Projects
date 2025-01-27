import os
from datetime import datetime
from pymongo import MongoClient
from bson import ObjectId,errors
from flask import Flask, jsonify, request, make_response, abort
import requests
from werkzeug.exceptions import BadRequest

api_url ="https://api.api-ninjas.com/v1/stockprice"
api_key = "k0VLa+SyAn9k8kEUvxeu9w==zmjWV76QR8w82Od8"
app = Flask(__name__)

# MongoDB Connection
client = MongoClient("mongodb://mongo:27017/")
db = client["stocks_db"]
collection = db[os.getenv('COLLECTION_NAME')]


@app.route('/kill', methods=['GET'])
def kill_container():
    os._exit(1)

@app.route('/stocks' , methods = ['POST','GET'])
def manage_stocks():
    if request.method == 'GET' :
        try:
            stocks = list(collection.find({}))
            for stock in stocks:
                stock["id"] = str(stock.get("_id"))
                del stock["_id"]
            return jsonify(stocks), 200
        except Exception as e:
            print("Exception: " , str(e))
            return jsonify({"server error":str(e)}), 500

    elif request.method == 'POST' :
        if request.content_type != "application/json":
                return jsonify({"error": "Expected application/json media type"}), 415
        try:
            data = request.json
            symbol = data['symbol'].upper()
            purchase_price = round(float(data['purchase price']), 2)
            shares = int(data['shares'])
            name = data.get('name' , 'NA')
            if 'purchase date' in data and data['purchase date']:
                if not datetime.strptime(data['purchase date'], "%d-%m-%Y"):
                    return jsonify({"error": "Malformed data"}),400
            purchase_date = data.get('purchase date' , 'NA')

            # Check for duplicate symbol
            if collection.find_one({"symbol": symbol}):
                return jsonify({"error": "Stock with the same symbol already exists"}), 400

            stock = {
                "name": name,
                "symbol": symbol,
                "purchase price": purchase_price,
                "purchase date": purchase_date,
                "shares": shares,
            }
            result = collection.insert_one(stock)
            
            return jsonify({"id": str(result.inserted_id)}), 201

        except (KeyError, ValueError,BadRequest):
            return jsonify({"error": "Malformed data"}), 400
        except TypeError:
            return jsonify({"error": "Expected application/json media type"}), 415    
        except Exception as e:
            return jsonify({"server error": str(e)}), 500


@app.route('/stocks/<string:id>', methods=['GET','PUT','DELETE'])
def stockByID(id):
    if request.method == 'GET' :
        try:
            stock = collection.find_one({"_id": ObjectId(id)})
            if stock:
                stock["id"] = str(stock.get("_id"))
                del stock["_id"]
                return jsonify(stock), 200
            else:
                return jsonify({"error": "Not found"}), 404

        except errors.InvalidId:
            return jsonify({"error": "Not found"}), 404
        except Exception as e:
            print("Exception: " , str(e))
            return jsonify({"server error":str(e)}), 500

    elif request.method == 'PUT' :
        if request.content_type != "application/json":
                return jsonify({"error": "Expected application/json media type"}), 415
        try:
            data = request.get_json()
            required_fields = ['id','name','symbol','purchase price', 'purchase date', 'shares']

            if not all(field in data for field in required_fields):
                return jsonify({"error": "Malformed data"}),400

            if data['purchase date']:
                if not datetime.strptime(data['purchase date'], "%d-%m-%Y"):
                    return jsonify({"error": "Malformed data"}),400

            collection.find_one_and_update(
                {"_id": ObjectId(id)},
                {"$set": data}
            )

            return jsonify({"id": id}), 200
        except errors.InvalidId:
            return jsonify({"error": "Not found"}), 404
        except (KeyError, ValueError, BadRequest):
            return jsonify({"error": "Malformed data"}), 400

        except Exception as e:
            print("Exception: ", str(e))
            return jsonify({"server error" : str(e)}),500


    elif request.method == 'DELETE':
        try:
            collection.find_one_and_delete({"_id": ObjectId(id)})
            return '',204

        except errors.InvalidId:
            return jsonify({"error":"Not found"}),404
        except Exception as e:
            print("Exception: ", str(e))
            return jsonify({"server error": str(e)}),500


@app.route('/stock-value/<string:stock_id>', methods=['GET'])
def stock_value(stock_id):
    try:
        stock = collection.find_one({"_id": ObjectId(stock_id)}, {"_id": 0})
        response = requests.get(
            f"https://api.api-ninjas.com/v1/stockprice?ticker={stock['symbol']}",
            headers={"X-Api-Key": api_key}
        )
        print(f"Fetching price for symbol: {stock['symbol']}")
        print(f"API response: {response.status_code}, {response.text}")

        if response.status_code != 200:
            return jsonify({"error": f"API response code: {response.status_code}"}), 500

        current_price = response.json().get('price', None)
        if current_price is None:
            return jsonify({"error": "Invalid API response: 'price' field missing"}), 500

        value = current_price * stock['shares']
        return jsonify({
            "symbol": stock['symbol'],
            "ticker": round(current_price, 2),
            "stock value": round(value, 2)
        }), 200
    except errors.InvalidId:
        return jsonify({"error":"Not found"}),404
    except Exception as e:
        return jsonify({"error": f"API response code: {response.status_code}"}), 500



@app.route('/portfolio-value', methods=['GET'])
def portfolio_value():
    total_value = 0.0
    stocks = collection.find({})
    for stock in stocks:
        response = requests.get(f"https://api.api-ninjas.com/v1/stockprice?ticker={stock['symbol']}",
                                headers={"X-Api-Key": api_key})
        data = response.json()
        if not data:
            return jsonify({"error": f"Symbol not found in the API, API response code: {response.status_code}"}), 500

        # Check if response is a list
        if isinstance(data, list):
            # Safely get the first element of the list
            stock_data = data[0]
            current_price = stock_data.get('price', 0.0)
        else:
            # If not a list, assume it's a dictionary
            current_price = data.get('price', 0.0)
        total_value += current_price * stock['shares']
    return jsonify({"date": datetime.now().strftime('%d-%m-%Y'), "portfolio value": round(total_value, 2)}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
