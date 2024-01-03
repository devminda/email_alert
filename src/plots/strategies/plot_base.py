from abc import ABC, abstractmethod
from typing import Any
import pandas as pd
from matplotlib.figure import Figure

class PlotBase(ABC):
    
    @abstractmethod
    def filter_data(self, data:pd.DataFrame, window=30, **args:Any)->pd.DataFrame:
        pass

    @abstractmethod
    def plot_data(self, data:pd.DataFrame, **args:Any)->Figure:
        pass
