from abc import ABC, abstractmethod
from typing import Dict, Any
import pandas as pd

class Strategybase(ABC):
    """Abstract class for signal calculation."""
    
    @staticmethod
    @abstractmethod
    def calculate_indicators(historical_data: pd.DataFrame, **kwargs) -> pd.DataFrame:
        """
        Calculate indicators based on historical data.

        Parameters:
        - historical_data (pd.DataFrame): Historical price data.
        - rolling_window (int): Rolling window size for calculations.

        Returns:
        pd.DataFrame: DataFrame with calculated indicators.
        """
        pass

    @abstractmethod
    def extract_latest_indicators(self, historical_data: pd.DataFrame, **kwargs) -> Dict[str, Any]:
        """
        Extract the latest indicators from historical data.

        Parameters:
        - historical_data (pd.DataFrame): Historical price data.
        - rolling_window (int): Rolling window size for calculations.

        Returns:
        Tuple[float, float, float, float, float, float]: Tuple of latest indicators.
        """
        pass

    @abstractmethod
    def generate_signals(self, historical_data: pd.DataFrame, **kwargs) -> int:
        """
        Generate trading signals based on historical data.

        Parameters:
        - historical_data (pd.DataFrame): Historical price data.
        - rolling_window (int): Rolling window size for calculations.

        Returns:
        int: Trading signal (1 for buy, 0 for hold/sell).
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """
        String representation of the strategy.

        Returns:
        str: String representation.
        """