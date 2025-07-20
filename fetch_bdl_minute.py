import yfinance as yf

def main():
    symbol = "BDL.NS"
    df = yf.download(symbol, interval="1m", period="7d")
    df.to_csv("BDL_last_week_minute.csv")

if __name__ == "__main__":
    main()
