import pandas as pd
import logging
from report_generator import generate_report


def analyze_stock(df ):
    try:
        df["Close"] = pd.to_numeric(df["Close"])
        df["Volume"] = pd.to_numeric(df["Volume"])
        return {"highest_close" : df["Close"].max(),
            "lowest_close" : df["Close"].min(),
            "average_volume" : df["Volume"].mean()}
    except Exception as e:
        logging.error(f"Error while analyzing data: {e}")
        return None