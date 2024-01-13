from enum import Enum
from src.plots.strategies.bb_adx_rsi_strategy import BollingerBandADXRSIStrategyPlot
from src.plots.strategies.yahoo_news_strategy import YahooFinanceNewsPlot

class Plots(Enum):
    bollinger_band_adx_rsi = BollingerBandADXRSIStrategyPlot
    yahoo_finance_news = YahooFinanceNewsPlot