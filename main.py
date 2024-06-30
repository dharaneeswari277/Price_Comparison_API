from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
import sqlite3

app = FastAPI()

# Database initialization and connection management
DB_PATH = "products.db"

def create_tables():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        retailer TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def get_db():
    conn = sqlite3.connect(DB_PATH)
    try:
        yield conn
    finally:
        conn.close()

# Data models
class Product(BaseModel):
    id: int
    name: str
    price: float
    retailer: str

class ProductCreate(BaseModel):
    name: str
    price: float
    retailer: str

# Mock data for different stores
mock_data = {
    "store1": [
        {"name": "Laptop", "price": 50000, "retailer": "Store 1"},
        {"name": "Mobile", "price": 20000, "retailer": "Store 1"},
        {"name": "Tablet", "price": 15000, "retailer": "Store 1"},
        {"name": "Smartwatch", "price": 8000, "retailer": "Store 1"},
        {"name": "Headphones", "price": 3000, "retailer": "Store 1"},
    ],
    "store2": [
        {"name": "Laptop", "price": 32000, "retailer": "Store 2"},
        {"name": "Mobile", "price": 14000, "retailer": "Store 2"},
        {"name": "Tablet", "price": 17000, "retailer": "Store 2"},
        {"name": "Smartwatch", "price": 9000, "retailer": "Store 2"},
        {"name": "Headphones", "price": 3500, "retailer": "Store 2"},
    ],
    "store3": [
        {"name": "Laptop", "price": 60000, "retailer": "Store 3"},
        {"name": "Mobile", "price": 30000, "retailer": "Store 3"},
        {"name": "Tablet", "price": 20000, "retailer": "Store 3"},
        {"name": "Smartwatch", "price": 10000, "retailer": "Store 3"},
        {"name": "Headphones", "price": 4000, "retailer": "Store 3"},
    ]
}


def insert_mock_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Check if there are any existing rows in the products table
    cursor.execute("SELECT COUNT(*) FROM products")
    count = cursor.fetchone()[0]
    
    if count == 0:
        # Insert mock data only if the table is empty
        for store, products in mock_data.items():
            for product in products:
                cursor.execute("""
                INSERT INTO products (name, price, retailer) VALUES (?, ?, ?)
                """, (product["name"], product["price"], product["retailer"]))
        conn.commit()
    else:
        print("Mock data already exists in the database. Skipping insertion.")
    
    conn.close()


# API endpoints.

# Adds a new product to the database. Request body should include product name, price, and retailer name.
@app.post("/api/products", response_model=Product)
def create_product(product: ProductCreate, db: sqlite3.Connection = Depends(get_db)):
    try:
        cursor = db.cursor()
        cursor.execute("""
        INSERT INTO products (name, price, retailer) VALUES (?, ?, ?)
        """, (product.name, product.price, product.retailer))
        product_id = cursor.lastrowid
        db.commit()
        return {"id": product_id, **product.dict()}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Error creating product: {e}")

# Returns a list of all products in the database.
@app.get("/api/products", response_model=List[Product])
def read_products(db: sqlite3.Connection = Depends(get_db)):
    try:
        cursor = db.cursor()
        cursor.execute("SELECT id, name, price, retailer FROM products")
        products = cursor.fetchall()
        return [{"id": id, "name": name, "price": price, "retailer": retailer} for id, name, price, retailer in products]
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Error reading products: {e}")

# Returns a list of products matching the search query, including the product name, price and retailer name.
@app.get("/api/product", response_model=List[Product])
def search_products(name: str, db: sqlite3.Connection = Depends(get_db)):
    try:
        cursor = db.cursor()
        cursor.execute("SELECT id, name, price, retailer FROM products WHERE name LIKE ?", (f"%{name}%",))
        products = cursor.fetchall()
        if not products:
            raise HTTPException(status_code=404, detail="Product not found")
        return [{"id": id, "name": name, "price": price, "retailer": retailer} for id, name, price, retailer in products]
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Error searching products: {e}")

# Initialize database and mock data on startup
create_tables()
insert_mock_data()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
