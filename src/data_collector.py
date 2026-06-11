import yfinance as yf

def get_stock_data (company):
    print (f"Downloading data for {company}")
    df = yf.download(company, period="1mo")
    df.to_csv(f"data/{company}.csv", index=False)
    print (f"Downloaded data for {company}")

