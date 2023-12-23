import yfinance as yf

def get_data(symbol="LOLCN0000.CM"):
    # Define the ticker symbol


    # Create a ticker object
    data = yf.download(symbol,period="2y", interval='1d')

    # Download historical data
    return data