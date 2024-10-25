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
            clean_columns = []
        for col in data.columns:
            if isinstance(col, tuple):
                # Remove the ticker suffix and clean up the name
                metric = col[0].replace(' ', '')  # Remove spaces
                clean_columns.append(metric)
            else:
                clean_columns.append('Date')
        data.columns = clean_columns
    
        # Convert to records and handle NaN values
        records = []
        for record in data.to_dict(orient='records'):
            processed_record = {}
            for key, value in record.items():
                # Convert numpy/pandas types to Python native types
                if pd.notnull(value):
                    if isinstance(value, (np.integer, np.floating)):
                        processed_record[key] = float(value)
                    else:
                        processed_record[key] = str(value)
                else:
                    processed_record[key] = None
            records.append(processed_record)
            
        return records

if __name__ == '__main__': 
      pass
