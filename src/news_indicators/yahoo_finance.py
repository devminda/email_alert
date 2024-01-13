from dotenv import load_dotenv
import os
from datetime import datetime
from typing import Any, Dict
import feedparser
import requests
import pandas as pd
import numpy as np
import time


# from news_indicator_base import NewsIndicatorBase
from src.news_indicators.news_indicator_base import NewsIndicatorBase

load_dotenv()

class YahooFinanceIndicator(NewsIndicatorBase):

    
    def get_news(self, **kwargs) -> Dict[str, Any]:
        
        rssfeedurl = f"https://feeds.finance.yahoo.com/rss/2.0/headline?s={kwargs['company_ticker']}&region=US&lang=en-US"

        news_feed = feedparser.parse(rssfeedurl)
        
        return news_feed
    
    def filter_data(self, data: Dict[str, Any])->list:
        # Define the format of the input string
        date_format = "%a, %d %b %Y %H:%M:%S %z"
        data_list=[]
        
        for news in data['entries']:
            data_dict = {}
            data_dict['title'] = news.title
            data_dict['summary'] = news.summary
            data_dict['published'] = datetime.strptime(news.published, date_format).date()
            data_list.append(data_dict)
        return data_list
    
    def calculate_sentiment(self, payload, max_retries=2, delay_seconds=2) -> list:
        API_URL = "https://api-inference.huggingface.co/models/mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis"
        headers = {"Authorization": f"Bearer {os.getenv('API_KEY')}"}
        
        for attempt in range(1, max_retries +1):
            try:
                response = requests.post(API_URL, headers=headers, json=payload)
                response.raise_for_status()
                return response.json()
            except requests.RequestException as e:
                print(f"Attempt {attempt}/{max_retries} failed. Error: {e}")
            if attempt < max_retries:
                print(f"Retrying in {delay_seconds} seconds...")
                time.sleep(delay_seconds)
            else:
                print("Max retries reached. Exiting.")
                return [[{'label': 'neutral', 'score': np.nan},
                            {'label': 'negative', 'score': np.nan},
                            {'label': 'positive', 'score': np.nan}]]

        
    
    def get_sentiment_for_news(self, data:Dict[str, Any])->pd.DataFrame:
        
        sentiment_list = []
        for article in data:
            article_cleaned = self.clean_data(article)
            output = self.calculate_sentiment(article_cleaned)[0]
            output = {item['label']: item['score'] for item in output}
            output['date'] = article['published']
            sentiment_list.append(output)

        data_table = pd.DataFrame(sentiment_list)
        
        if data_table.empty:
            return pd.DataFrame(columns=['positive', 'negative','neutral'])
        else:
            grouped_data = data_table.groupby('date')[['positive', 'negative','neutral']].mean()
            grouped_data = grouped_data.rename_axis('Date')
            return grouped_data
    
    
    def clean_data(self, data:Dict[str, Any])->str:
        output = "/n".join([data['title'], data['summary']])
        return output
    
    def yahoo_sentiment(self, historical_data:pd.DataFrame, symbol:str)->pd.DataFrame:
        data = self.get_news(company_ticker=symbol)
        data_dict = self.filter_data(data)
        data_last = self.get_sentiment_for_news(data_dict)
        
        data_df = historical_data.join( data_last, how='left')
        
        return data_df

# if __name__ == "__main__":
#     obj = YahooFinanceIndicator()
#     data = obj.get_news(company_ticker='AAPL1')
#     data_dict = obj.filter_data(data)
#     print(data_dict)
#     data_last = obj.get_sentiment_for_news(data_dict)
#     print(data_last)

    # print(data_dict)