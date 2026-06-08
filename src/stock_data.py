import yfinance as yf

company = "TCS.NS"
ticker = yf.Ticker(company)
info = ticker.info

def save_company_data (company):
    print (f"Downloading data for {company}")
    df = yf.download(company, period="1mo")
    df.to_csv(f"data/{company}.csv", index=False)
    print (f"Downloaded data for {company}")

save_company_data(company)