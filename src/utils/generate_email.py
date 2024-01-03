from dotenv import load_dotenv
import os
import base64
from io import BytesIO

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import ssl
from datetime import datetime
import smtplib
from typing import List

from src.models.strategies.strategy_base import Strategybase
from src.data_operations.data_retrieval import get_data
from src.plots.strategies.plot_base import PlotBase

from data.email_list import email_list
from src.utils.email_body import html_body
import matplotlib.pyplot as plt

load_dotenv()

def generate_emails(symbols:List[str], strategy:Strategybase, plots:PlotBase, **params):
    
    
    gmail_user = 'hmoemailtester@gmail.com'
    gmail_password = os.getenv('GMAIL_PASSWORD')
    
    subject = f"{datetime.today()} [Strategy: {strategy()}]"

    
    table_rows = ""
    msg = MIMEMultipart()
    for symb in symbols:
        historical_data = get_data(symb)
        strat = strategy()
        df = strat.calculate_indicators(historical_data, **params['stratergy'])
        indicators = strat.get_indicators(df, **params['stratergy'])
        indicators_str = ", ".join([f"{key.upper()}: {value}" for key, value in indicators.items()])

        if strat.signals(df, **params['stratergy'])==1:
            table_rows += f"<tr><td>{symb}</td><td style=color:green><b>Signal</b></td><td>{indicators_str}</td></tr>"
        else:

            table_rows += f"<tr><td>{symb}</td><td style=color:red><b>No Signal</b></td><td>{indicators_str}</td></tr>"

        plot_diagram = plots()
        plot_df = plot_diagram.filter_data(df, **params['plot'])
        plot_fig = plot_diagram.plot_data(plot_df, **params['plot'])
        
        plot_buf = BytesIO()
        plot_fig.savefig(plot_buf, format='png')
        plot_buf.seek(0)

        plt.close()

        img = MIMEImage(plot_buf.read())

        img.add_header('Content-Disposition', 'attachment', filename=f'{symb}.png')
        img.add_header('Content-ID', f'<{symb}>')
        msg.attach(img)
        

    html_body1 = html_body.format(table_rows=table_rows)
    
    msg.attach(MIMEText(html_body1, 'html'))    
    
    msg['From'] = gmail_user
    msg['To'] =  ", ".join(email_list)
    msg['Subject'] = subject
    

    context = ssl.create_default_context()

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user, email_list, msg.as_string())
    server.close()
    # os.remove('plot.png')