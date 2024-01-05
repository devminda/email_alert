from abc import ABC, abstractmethod
from typing import Any
import pandas as pd
from matplotlib.figure import Figure

class PlotBase(ABC):
    
    @staticmethod
    @abstractmethod
    def filter_data(data:pd.DataFrame, window=30, **kwargs:Any)->pd.DataFrame:
        pass

    @abstractmethod
    def plot_data(self, data:pd.DataFrame, **kwargs:Any)->Figure:
        pass
