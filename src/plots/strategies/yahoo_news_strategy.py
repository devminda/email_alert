from pandas.core.frame import DataFrame
from src.plots.strategies.plot_base import PlotBase
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

class YahooFinanceNewsPlot(PlotBase):
            
    @staticmethod
    def filter_data(data,**kwargs):
        data = data.iloc[-kwargs.get('window'):].copy()
        return data
    
    
    
    def plot_data(self, data: DataFrame, **kwargs) -> Figure:
          # Adjust the overall figure size as needed
        fig, ax = plt.subplots()

        # Plot the function
        ax.plot( data['Close'], label="Stock Price")
        plt.xticks(data.index, rotation=90, ha='right', fontsize=6)

        # Set labels and title
        ax.set(title='Stock Prices')

        # Show grid
        ax.grid(True)

        # Show legend
        ax.legend()
        fig.suptitle(f"{kwargs.get('title')}", fontsize=18)
        fig.subplots_adjust(top=0.88)
        return fig
        
