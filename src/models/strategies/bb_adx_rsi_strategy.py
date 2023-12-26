
"""Uses ADX, RSI and Bollinger bands to calculate signals"""
from src.models.strategies.strategy_base import Strategybase
import pandas as pd
import pandas_ta as ta

class BollingerBandADXRSIStrategy(Strategybase):
    def calculate_indicators(self, historical_data, roll=7)->pd.DataFrame:
        historical_data['rsi'] = ta.rsi(pd.Series(historical_data['Close']), roll)
        historical_data[[f'BBL_{str(roll)}_3.0',f'BBM_{str(roll)}_3.0',f'BBU_{str(roll)}_3.0']] = historical_data.ta.bbands(roll,3)[[f'BBL_{str(roll)}_3.0',f'BBM_{str(roll)}_3.0',f'BBU_{str(roll)}_3.0']]
        historical_data[f'ADX_{str(roll)}'] = ta.adx(historical_data['High'], historical_data['Low'],historical_data['Close'], roll)[f'ADX_{str(roll)}']

        return historical_data

    def get_indicators(self, historical_data: pd.DataFrame, roll=7) -> tuple:
        close = historical_data.iloc[-1][ 'Close']
        adx = historical_data.iloc[-1][ f'ADX_{roll}']
        rsi = historical_data.iloc[-1][ 'rsi']
        bu = historical_data.iloc[-1][ f'BBU_{roll}_3.0']
        bl = historical_data.iloc[-1][ f'BBL_{roll}_3.0']
        bm = historical_data.iloc[-1][ f'BBM_{roll}_3.0']
        return {"close": close, "adx":adx, "rsi":rsi, "bu":bu, "bl":bl, "bm":bm}

    def signals(self,historical_data: pd.DataFrame, roll=7)-> int:
        indicators = self.get_indicators(historical_data, roll)
        if (indicators.get("adx")>25) and (indicators.get("rsi")<30) and (indicators.get("close")<indicators.get("bl")):
            return 1
        else:
            return 0
    
    def __str__(self) -> str:
        return "BollingerBand ADX RSI Strategy"