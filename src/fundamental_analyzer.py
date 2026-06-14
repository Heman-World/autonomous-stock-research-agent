import yfinance as yf
from config import DEFAULT_TICKER

def get_fundamentals(DEFAULT_TICKER):
    stock = yf.Ticker(DEFAULT_TICKER)
    info = stock.info
    return {"market_cap":info.get("marketCap"), "pe_ratio":info.get("trailingPE"), "dividend_yield":info.get("dividendYield"),
    "sector":info.get("sector"), "industry":info.get("industry")}