"""Uses yahoo news sentiment to calculate signals"""
from src.models.strategies.strategy_base import Strategybase
from src.news_indicators.yahoo_finance import YahooFinanceIndicator
import pandas as pd
import pandas_ta as ta

class YahooNewsStrategy(Strategybase):

    @staticmethod
    def calculate_indicators(historical_data:pd.DataFrame, symbol:str, **kwargs)->pd.DataFrame:
        obj = YahooFinanceIndicator()
        historical_data = obj.yahoo_sentiment(historical_data, symbol)
        
        return historical_data

    def extract_latest_indicators(self, historical_data: pd.DataFrame, **kwargs) -> dict:
        
        positive = historical_data.iloc[-1]['positive']
        negative = historical_data.iloc[-1]['negative']
        neutral = historical_data.iloc[-1]['neutral']
        close = historical_data.iloc[-1]['Close']
        return {"close": close, "positive":positive, "negative":negative, "neutral":neutral}

    def generate_signals(self,historical_data: pd.DataFrame, **kwargs)-> int:
        indicators = self.extract_latest_indicators(historical_data)
        print(indicators)
        if (indicators.get("positive")>0.5) and (indicators.get("negative")<0.1):
            return 1
        else:
            return 0
    
    def __str__(self) -> str:
        return "Yahoo Finance News Strategy"