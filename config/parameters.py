from enum import Enum

class Parameters(Enum):
    bollinger_band_adx_rsi = {'model':{'rolling_window': 7},
                              'plot': {'rolling_window': 7,'window':30},
                              'description':"When the Relative Strength Index (RSI) falls below 30 and the Average Directional Index (ADX) exceeds 25, it suggests an oversold condition accompanied by a robust trend. A buy signal is generated when the closing price dips below the lower Bollinger band, and simultaneously, the RSI is below 30, and the ADX is above 25."
    }

    yahoo_finance_news = {'model': {},
                          'plot':{'window':30},
                          'description': "Sentiment score based strategy. The latest news from Yahoo finance is obtained and a sentiment score is calculated to check if market has a positive or negative sentiment. If the sentiment is positive it indicates a buy signal."}

