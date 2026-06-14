import yfinance as yf
import logging
from config import DATA_FOLDER
import pandas as pd
def get_stock_data (company):
    try:
        logging.info(f"Downloading data for {company}")
        df = yf.download(company, period="1mo")
        if df.empty:
            logging.error(f"No data found for {company}")
            return None
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
        df.to_csv(f"{DATA_FOLDER}/{company}.csv", index=False)
        return df
    except Exception as e:
        logging.error(f"Error downloading data: {e}")
        return None
