from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

STOCKS1_URL = "http://stocks1-a:8000"
STOCKS2_URL = "http://stocks2:8000"
API_NINJA_URL = "https://api.api-ninjas.com/v1/stockprice"
API_NINJA_KEY = "k0VLa+SyAn9k8kEUvxeu9w==zmjWV76QR8w82Od8"

def fetch_current_price(symbol):
    """Fetch the current price of a stock from API Ninja."""
    try:
        response = requests.get(
            f"https://api.api-ninjas.com/v1/stockprice?ticker={symbol}",
            headers={"X-Api-Key": API_NINJA_KEY}
        )
        current_price = response.json().get('price', None)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        return float(current_price)  # Return the price or 0 if not found
    except requests.exceptions.RequestException as e:
        print(f"Error fetching price for {symbol}: {e}")
        return 0  # Return 0 if there's an error

@app.route('/capital-gains', methods=['GET'])
def capital_gains():
    query = request.args
    portfolio = query.get('portfolio')  # Handle the 'portfolio' query parameter
    numsharesgt = query.get('numsharesgt')
    numshareslt = query.get('numshareslt')

    # Determine which portfolios to query
    if portfolio == 'stocks1':  # Check if 'portfolio=stocks1'
        urls = [STOCKS1_URL]
    elif portfolio == 'stocks2':  # Check if 'portfolio=stocks2'
        urls = [STOCKS2_URL]
    else:
        urls = [STOCKS1_URL, STOCKS2_URL]

    total_gain = 0
    for url in urls:
        try:
            response = requests.get(f"{url}/stocks")
            response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
            stocks = response.json()

            for stock in stocks:
                # Ensure the stock has the required keys
                if 'purchase price' not in stock or 'shares' not in stock or 'symbol' not in stock:
                    print(f"Skipping invalid stock: {stock}")
                    continue

                # Fetch the current price from API Ninja
                current_price = fetch_current_price(stock['symbol'])

                # Filter based on numsharesgt and numshareslt
                if numsharesgt and stock['shares'] <= int(numsharesgt):
                    continue
                if numshareslt and stock['shares'] >= int(numshareslt):
                    continue

                # Calculate the capital gain for this stock
                capital_gain = (current_price - stock['purchase price']) * stock['shares']
                total_gain += capital_gain
        except requests.exceptions.RequestException as e:
            # Log the error and continue
            print(f"Error fetching stocks from {url}: {e}")
            continue

    return str(total_gain)  # Return the float as a string

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)