import pandas_ta as ta
import pandas as pd


def calculates_technical_indicators(historical_data, roll=7):
    historical_data['rsi'] = ta.rsi(pd.Series(historical_data['Close']), roll)
    historical_data[[f'BBL_{str(roll)}_3.0',f'BBM_{str(roll)}_3.0',f'BBU_{str(roll)}_3.0']] = historical_data.ta.bbands(roll,3)[[f'BBL_{str(roll)}_3.0',f'BBM_{str(roll)}_3.0',f'BBU_{str(roll)}_3.0']]
    historical_data[f'ADX_{str(roll)}'] = ta.adx(historical_data['High'], historical_data['Low'],historical_data['Close'], roll)[f'ADX_{str(roll)}']

    return historical_data