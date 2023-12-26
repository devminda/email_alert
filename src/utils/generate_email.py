from dotenv import load_dotenv
import os

from email.mime.text import MIMEText
import ssl
from datetime import datetime
import smtplib
from typing import List
from src.models.strategies.strategy_base import Strategybase
from src.data_operations.data_retrieval import get_data

from data.email_list import email_list
from src.utils.email_body import html_body

load_dotenv()

def generate_emails(symbols:List[str], strategy:Strategybase, **params):
    
    
    gmail_user = 'hmoemailtester@gmail.com'
    gmail_password = os.getenv('GMAIL_PASSWORD')
    print(gmail_password)
    subject = f"{datetime.today()} [Strategy: {strategy()}]"

     
    table_rows = ""
    for symb in symbols:
        historical_data = get_data(symb)
        strat = strategy()
        df = strat.calculate_indicators(historical_data, **params)
        indicators = strat.get_indicators(df, **params)
        indicators_str = ", ".join([f"{key.upper()}: {value}" for key, value in indicators.items()])

        if strat.signals(df, **params)==1:
            table_rows += f"<tr><td>{symb}</td><td style=color:green><b>Signal</b></td><td>{indicators_str}</td></tr>"
        else:

            table_rows += f"<tr><td>{symb}</td><td style=color:red><b>No Signal</b></td><td>{indicators_str}</td></tr>"
                

    html_body1 = html_body.format(table_rows=table_rows)
    em = MIMEText(html_body1, 'html')
    em['From'] = gmail_user
    em['To'] =  ", ".join(email_list)
    em['Subject'] = subject
    

    context = ssl.create_default_context()

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user, email_list, em.as_string())
    server.close()