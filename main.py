from email.message import EmailMessage
import ssl
import smtplib

from utils.signals import calculate_signal, signals
from utils.technical_indicators import calculates_technical_indicators
from utils.data_retrieval import get_data

symbols =  ['AAPL', 'NVDA', 'PYPL', 'GC=F']


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
        df = calculates_technical_indicators(historical_data, 7)
        close, adx, rsi, bu, bl, bm = calculate_signal(historical_data, 7)

        if signals(historical_data, 7)==1:
            msg = msg + f"{symb}: the signal is 1 best time to buy at {df.loc[-1, 'Close']}\n"

        else:
            msg = msg + f"{symb} no signal\n" + f"close:{close}, adx:{adx}, rsi:{rsi}, bu:{bu}, bl:{bl}, bm:{bm}\n\n"
    em.set_content(msg)

    context = ssl.create_default_context()

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user, gmail_user, em.as_string())
    server.close()

if __name__=="__main__":
    some_job()