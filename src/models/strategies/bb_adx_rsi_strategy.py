"""Uses ADX, RSI and Bollinger bands to calculate signals"""
from src.models.strategies.strategy_base import Strategybase
import pandas as pd
import pandas_ta as ta
from typing import Dict, Any

class BollingerBandADXRSIStrategy(Strategybase):

    @staticmethod
    def calculate_indicators(historical_data:pd.DataFrame, rolling_window:int=7, **kwargs)->pd.DataFrame:
        historical_data['rsi'] = ta.rsi(pd.Series(historical_data['Close']), rolling_window)
        historical_data[[f'BBL_{str(rolling_window)}_3.0',f'BBM_{str(rolling_window)}_3.0',f'BBU_{str(rolling_window)}_3.0']] = historical_data.ta.bbands(rolling_window,3)[[f'BBL_{str(rolling_window)}_3.0',f'BBM_{str(rolling_window)}_3.0',f'BBU_{str(rolling_window)}_3.0']]
        historical_data[f'ADX_{str(rolling_window)}'] = ta.adx(historical_data['High'], historical_data['Low'],historical_data['Close'], rolling_window)[f'ADX_{str(rolling_window)}']

        return historical_data

    def extract_latest_indicators(self, historical_data: pd.DataFrame, rolling_window:int=7, **kwargs) -> Dict[str,Any]:
        close = historical_data.iloc[-1][ 'Close']
        adx = historical_data.iloc[-1][ f'ADX_{rolling_window}']
        rsi = historical_data.iloc[-1][ 'rsi']
        bu = historical_data.iloc[-1][ f'BBU_{rolling_window}_3.0']
        bl = historical_data.iloc[-1][ f'BBL_{rolling_window}_3.0']
        bm = historical_data.iloc[-1][ f'BBM_{rolling_window}_3.0']
        return {"close": close, "adx":adx, "rsi":rsi, "bu":bu, "bl":bl, "bm":bm}

    def generate_signals(self,historical_data: pd.DataFrame, rolling_window:int=7, **kwargs)-> int:
        indicators = self.extract_latest_indicators(historical_data, rolling_window)
        if (indicators.get("adx")>25) and (indicators.get("rsi")<30) and (indicators.get("close")<indicators.get("bl")):
            return 1
        else:
            return 0
    
    def __str__(self) -> str:
        return "BollingerBand ADX RSI Strategy"