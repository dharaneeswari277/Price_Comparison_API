# Price_Comparison_API

This is a simple Price Comparison API built using Flask. It allows users to search for product prices across multiple online stores.

Features
Search Products: Search for products across multiple online stores using GET and POST requests.
Consolidated Results: Get a consolidated list of product prices from different stores.

Dummy Data

The API uses mock data for three online stores, each with a list of products and prices:
Store1
Store2
Store3

Installation 
Clone the repository:
git clone https://github.com/yourusername/price-comparison-api.git
cd price-comparison-api

Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install the required dependencies:
pip install fastapi uvicorn sqlalchemy databases
pip install Flask

Usage
Run the application:
uvicorn main:app --reload

Endpoints:

GET /api/products: Search for products by name.

Query Parameters:
product_name: Name of the product to search for.

Example:
curl "http://127.0.0.1:8000/api/products?product_name=Product A"

POST /search: Search for products by name.

JSON Body:
product_name: Name of the product to search for.

Example:
curl -X POST -H "Content-Type: application/json" -d '{"product_name': 'Product A'}" "htttp://127.0.0.1:8000/api/products"

Request:
curl "http://127.0.0.1:8000/api/products?name=Product A"


Contact:
For any questions or suggestions, please contact dharaneeswari277a@gmail.com
