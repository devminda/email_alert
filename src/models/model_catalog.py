from enum import Enum
from src.models.strategies.bb_adx_rsi_strategy import BollingerBandADXRSIStrategy
from src.models.strategies.yahoo_news_startegy import YahooNewsStrategy

class Strategies(Enum):
    bollinger_band_adx_rsi = BollingerBandADXRSIStrategy
    yahoo_finance_news = YahooNewsStrategy

