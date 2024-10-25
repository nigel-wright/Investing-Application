from flask import Flask, request, jsonify, abort
from flask_cors import CORS
import pandas as pd
from fetch_data import *
import os

app = Flask(__name__)
CORS(app)

# Endpoint to search for stock data by a query value
@app.route('/api/search/<string:ticker>', methods=['GET'])
def search(ticker):
    try: 
        data = get_ticker_data(ticker)
        data = process_stock_data(data)

        return jsonify({
            'status': 'success',
            'ticker': ticker,
            'data': data
        }), 200

    except Exception as e: 
        return jsonify({
            'status': 'error',
            'message': str(e),
            'ticker': ticker
        }), 400

# Main route to test if the server is running
@app.route('/', methods=['GET'])
def home():
    return "Flask backend is running. Use the /search endpoint to search stock data."

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=3000)
