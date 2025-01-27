from logging import exception
from datetime import datetime
from flask import Flask, jsonify, request, make_response, abort
import requests
import uuid

api_url ="https://api.api-ninjas.com/v1/stockprice"
api_key = "k0VLa+SyAn9k8kEUvxeu9w==zmjWV76QR8w82Od8"
app = Flask(__name__)
stocks ={}

@app.route('/stocks' , methods = ['POST','GET'])
def manage_stocks():
    if request.method == 'GET' :
        try:
            return jsonify(list(stocks.values())), 200
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

            if any(stock['symbol'] == symbol for stock in stocks.values()):
                return jsonify({"error": "Stock with the same symbol already exist"}), 400

            stock_id = str(uuid.uuid4())
            stocks[stock_id] = {
                "id": stock_id,
                "name": name,
                "symbol": symbol,
                "purchase price": purchase_price,
                "purchase date": purchase_date,
                "shares": shares,
            }
            
            return jsonify({"id": stock_id}), 201

        except KeyError:
            return jsonify({"error": "Malformed data"}), 400
        except ValueError:
            return jsonify({"error": "Malformed data"}),400
        except TypeError:
            return jsonify({"error": "Expected application/json media type"}), 415    
        except Exception as e:
            return jsonify({"server error": str(e)}), 500


@app.route('/stocks/<string:id>', methods=['GET','PUT','DELETE'])
def stockByID(id):
    if request.method == 'GET' :
        try:
            if id in stocks:
                return jsonify(stocks[id]), 200
            else:
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
            if not stocks[id]:
                print("PUT error: no such ID")
                return jsonify({"error":"Not found"}),404
            if data['purchase date']:
                if not datetime.strptime(data['purchase date'], "%d-%m-%Y"):
                    return jsonify({"error": "Malformed data"}),400
            stock = {
                'id': id,
                'name' : data['name'],
                'symbol' : data['symbol'],
                'purchase price' : data['purchase price'],
                'purchase date' : data['purchase date'],
                'shares' : data['shares'],
            }
            stocks[id] = stock
            response = {"id":id}
            return jsonify(response),200
        except KeyError:
            return jsonify({"error": "Malformed data"}), 400
        except ValueError:
            return jsonify({"error": "Malformed data"}),400
        except Exception as e:
            print("Exception: ", str(e))
            return jsonify({"server error" : str(e)}),500

    elif request.method == 'DELETE':
        try:
            del stocks[id]
            return '',204
        except KeyError:
            print("DELETE request error, no such ID")
            return jsonify({"error":"Not found"}),404
        except Exception as e:
            print("Exception: ", str(e))
            return jsonify({"server error": str(e)}),500


@app.route('/stock-value/<string:stock_id>', methods=['GET'])
def stock_value(stock_id):
    if stock_id not in stocks:
        return jsonify({"error": "Not found"}), 404

    stock = stocks[stock_id]
    try:
        print(f"Fetching price for symbol: {stock['symbol']}")
        response = requests.get(
            f"https://api.api-ninjas.com/v1/stockprice?ticker={stock['symbol']}",
            headers={"X-Api-Key": api_key}
        )
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

    except Exception as e:
        return jsonify({"error": f"API response code: {response.status_code}"}), 500



@app.route('/portfolio-value', methods=['GET'])
def portfolio_value():
    total_value = 0.0
    for stock_id, stock in stocks.items():
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
    app.run(host="0.0.0.0", port=5001, debug=True)
