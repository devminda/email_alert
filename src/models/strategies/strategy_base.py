from abc import ABC, abstractmethod
from typing import Tuple
import pandas as pd

class Strategybase(ABC):
    """Abstract class for signal calculation."""
    
    @staticmethod
    @abstractmethod
    def calculate_indicators(historical_data: pd.DataFrame, rolling_window: int = 7, **kwargs) -> pd.DataFrame:
        """
        Calculate indicators based on historical data.

        Parameters:
        - historical_data (pd.DataFrame): Historical price data.
        - rolling_window (int): Rolling window size for calculations.

        Returns:
        pd.DataFrame: DataFrame with calculated indicators.
        """

    @abstractmethod
    def extract_latest_indicators(self, historical_data: pd.DataFrame, rolling_window: int = 7, **kwargs) -> Tuple[float, float, float, float, float, float]:
        """
        Extract the latest indicators from historical data.

        Parameters:
        - historical_data (pd.DataFrame): Historical price data.
        - rolling_window (int): Rolling window size for calculations.

        Returns:
        Tuple[float, float, float, float, float, float]: Tuple of latest indicators.
        """

    @abstractmethod
    def generate_signals(self, historical_data: pd.DataFrame, rolling_window: int = 7, **kwargs) -> int:
        """
        Generate trading signals based on historical data.

        Parameters:
        - historical_data (pd.DataFrame): Historical price data.
        - rolling_window (int): Rolling window size for calculations.

        Returns:
        int: Trading signal (1 for buy, 0 for hold/sell).
        """

    @abstractmethod
    def __str__(self) -> str:
        """
        String representation of the strategy.

        Returns:
        str: String representation.
        """