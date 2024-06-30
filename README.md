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

git clone https://github.com/dharaneeswari277/Price_Comparison_API.git

cd Price_Comparison_API

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

1. GET /api/products: Search for products by name.

Query Parameters:

name: Name of the product to search for.

Example:

curl "http://127.0.0.1:8000/api/product?name=Laptop"


2. POST /api/products: Search for products by name.

JSON Body:

name: Name of the product to search for.

Example:

Post data in the form of json in POSTMAN

curl -X POST -H "Content-Type: application/json" -d '{"name': 'Laptop'}" "http://127.0.0.1:8000/api/products"

Request:

curl "http://127.0.0.1:8000/api/product?name=Laptop"

3. GET /api/products: Returns a list of all products in the database.

Example:
curl "http://127.0.0.1:8000/api/products"

Database

This project uses SQLite as the database for storing product information. SQLite was chosen for the following reasons:


Simplicity: SQLite is a self-contained, serverless database engine that is easy to set up and use.

Lightweight: It has a small footprint, making it ideal for small to medium-sized applications.

No Configuration Required: It doesn’t require a separate server process, and the database can be created simply by opening a file.

Database Schema

The products table has the following columns:

id: Integer, primary key, auto-incremented.

name: Text, name of the product.

price: Real, price of the product.

retailer: Text, name of the retailer.

Contact:

For any questions or suggestions, please contact dharaneeswari277a@gmail.com
