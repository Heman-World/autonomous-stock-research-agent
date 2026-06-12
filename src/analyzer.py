import pandas as pd
from report_generator import generate_report

def analyze_stock(df ):
   df["Close"] = pd.to_numeric(df["Close"])
   df["Volume"] = pd.to_numeric(df["Volume"])
   return {"highest_close" : df["Close"].max(),
    "lowest_close" : df["Close"].min(),
    "average_volume" : df["Volume"].mean()}