import pandas as pd
import numpy as np 
import yfinance as yf
import requests
import os
import json
from datetime import datetime, timedelta

# get ticker info for last 15 days
def get_ticker_data(tickers):
        # define start and end date
        end = datetime.now()
        start = end - timedelta(days=15)

        # download stock data from yfinance
        data = yf.download(tickers=tickers, 
                     start=start, 
                     end=end)
    
        # return the date
        return data
    
def process_stock_data(data):
        # Reset the index to make the date a column
        data = data.reset_index()
        
        # Convert dates to strings
        data['Date'] = data['Date'].dt.strftime('%Y-%m-%d')
        
        # Handle multi-index columns if present
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = [
                '_'.join(col) if isinstance(col, tuple) else col 
                for col in data.columns
            ]
        
        # Convert to records and handle NaN values
        records = []
        for record in data.to_dict(orient='records'):
            processed_record = {}
            for key, value in record.items():
                processed_record[key] = value if pd.notnull(value) else None
            records.append(processed_record)
            
        return records
      

if __name__ == '__main__': 
      pass
