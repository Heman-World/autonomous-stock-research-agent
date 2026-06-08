import yfinance as yf

company = "TCS.NS"
ticker = yf.Ticker(company)
info = ticker.info

def save_company_data (company):
    df = yf.download(company, period="1mo")
    df.to_csv(f"data/{info.get("longName")}.csv", index=False)


save_company_data(company)