import pandas as pd
from stock_data import company

def analyze_stock(company):
    df = pd.read_csv(f'data/{company}.csv', skiprows=[1])
    df["Close"] = pd.to_numeric(df["Close"])
    df["Volume"] = pd.to_numeric(df["Volume"])
    return {"highest_close" : df["Close"].max(),
    "lowest_close" : df["Close"].min(),
    "average_volume" : df["Volume"].mean()}

print(analyze_stock(company))