from abc import ABC, abstractmethod
from typing import Any
import pandas as pd

class Strategybase(ABC):
    """Abstract class for signal calculation."""
    
    @abstractmethod
    def calculate_indicators(self, data: pd.DataFrame,*args:Any)->pd.DataFrame:
        """Calculates the indicators"""
        pass

    @abstractmethod
    def get_indicators(self, data: pd.DataFrame, *args:Any) -> tuple:
        """Passes the indicators in a tuple"""
        pass

    @abstractmethod
    def signals(self, data: pd.DataFrame, *args:Any) -> int:
        """Returns signals based on the calculated signals and the startegy used 

        Args:
            data (pd.DataFrame): historical data

        Returns:
            int: 1 if signal exist, 0 if signal is not there
        """
    