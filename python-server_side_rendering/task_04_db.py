import json
import os
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r') as f:
        data = json.load(f)
    items_list = data.get('items', [])
    return render_template('items.html', items=items_list)
def get_products_from_db():
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]
    except Exception as e:
        raise Exception(f"Database error: {str(e)}")

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products = []
    error = None

    try:
        if source == "json":
            with open('products.json', 'r', encoding='utf-8') as f:
                products = json.load(f)

        elif source == "csv":
            with open('products.csv', 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                products = list(reader)

        elif source == "sql":
            products = get_products_from_db()

        else:
            error = "Wrong source"
            return render_template('product_display.html', error=error)

        if product_id:
            products = [p for p in products if int(p['id']) == product_id or p.get('id') == product_id]
            if not products:
                error = "Product not found"
                return render_template('product_display.html', error=error)

        return render_template('product_display.html', products=products)

    except Exception as e:
        error = f"Error: {str(e)}"
        return render_template('product_display.html', error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)