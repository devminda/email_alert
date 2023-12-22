import yfinance as yf
# from apscheduler.schedulers.blocking import BlockingScheduler
from email.message import EmailMessage
import ssl
import smtplib


symbols =  ['AAPL', 'NVDA', 'PYPL', 'GC=F']

def get_data(symbol="AAPL"):
    # Define the ticker symbol
    

    # Create a ticker object
    data = yf.download(symbol,start="2023-01-01", interval='1d')

    # Download historical data
    return data

def test_engulfing(df):
    last_open = df.iloc[-1, :].Open
    last_close = df.iloc[-1, :].Close
    previous_open = df.iloc[-2, :].Open
    previous_close = df.iloc[-2, :].Close

    if (previous_open < previous_close 
        and last_open > previous_close 
        and last_close < previous_open):
        return 1  # Bearish Engulfing Pattern
    
    elif (previous_open > previous_close
          and last_open < previous_close 
          and last_close > previous_open):
        return 2  # Bullish Engulfing Pattern
    else:
        return 0  # No Engulfing Pattern

def some_job():
  
    em = EmailMessage()

    gmail_user = 'hmoemailtester@gmail.com'
    gmail_password = 'eszftczfphgwqpjj'
    subject = 'info signal'
    msg="Trading Signal Message \n"
    em['From'] = gmail_user
    em['To'] = gmail_user
    em['Subject'] = subject
    for symb in symbols:
        historical_data = get_data(symb)
        if test_engulfing(historical_data)==1:
            msg = msg + str(symb+": the signal is 1 bearish") + "\n"

        elif test_engulfing(historical_data)==2:
            msg = msg + str(symb+": the signal is 2 bullish") + "\n"
        else:
            msg = msg + f"{symb} no signal\n"

    em.set_content(msg)

    context = ssl.create_default_context()

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user, gmail_user, em.as_string())
    server.close()

if __name__=="__main__":
    some_job()