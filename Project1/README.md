# Project 1: Stock Portfolio Management

This project is a Dockerized RESTful application designed to manage stock portfolios. It offers features to add, update, retrieve, and delete stocks, calculate individual stock values, and compute the total portfolio value using real-time stock prices fetched from an external API.

## Features

- **Portfolio Management:** Add, update, and delete stocks in a portfolio with unique IDs.  
- **Stock Value Calculation:** Dynamically calculate the current value of individual stocks based on real-time prices.  
- **Portfolio Valuation:** Compute the total value of the portfolio using the latest stock data.  
- **RESTful Endpoints:** Exposes clean and structured JSON-based APIs for all operations.  
- **Containerized Deployment:** Runs seamlessly in a Docker container for easy setup and portability.  

## REST API Endpoints

- **`GET /stocks`**: Retrieve a list of all stocks in the portfolio.  
- **`POST /stocks`**: Add a new stock to the portfolio. Requires fields such as `symbol`, `purchase price`, and `shares`.  
- **`GET /stocks/{id}`**: Retrieve details of a specific stock by its unique ID.  
- **`PUT /stocks/{id}`**: Update the details of an existing stock.  
- **`DELETE /stocks/{id}`**: Remove a stock from the portfolio.  
- **`GET /stock-value/{id}`**: Fetch the current value of a specific stock, calculated using its real-time price and quantity.  
- **`GET /portfolio-value`**: Compute and retrieve the total value of the entire portfolio.  

## Technologies Used

- **Programming Language:** Python (Flask)  
- **Containerization:** Docker  
- **External API:** [API Ninjas Stock Price API](https://api-ninjas.com/api/stockprice)  

## Setup and Usage

1. **Prerequisites:**  
   - Install [Docker](https://www.docker.com/).  
   - Obtain an API key from [API Ninjas Stock Price API](https://api-ninjas.com/).  

2. **Build and Run the Docker Container:**  
   ```bash
   docker build -t stock-portfolio-app .  
   docker run -p 5001:5001 -e API_KEY=<your_api_key> stock-portfolio-app  
3. **Access the Application:**
The API will be available at http://localhost:5001. Use tools like Postman or curl to interact with the endpoints.

## Example Request and Response

Adding a Stock (POST /stocks)
Request:

{
  "symbol": "AAPL",
  "purchase price": 150.00,
  "purchase date": 12-12-2024,
  "name": "Apple Inc.",
  "shares": 10
}

Response:

{
  "id": "12345"
}

Calculating Portfolio Value (GET /portfolio-value)
Response:

{
  "date": "27-01-2025",
  "portfolio value": 5000.00
}


## Acknowledgments
This project was part of a cloud computing course at Reichman University. Special thanks to Dr. Daniel Yellin for his guidance and resources.

---
