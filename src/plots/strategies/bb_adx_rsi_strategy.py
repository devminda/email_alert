from pandas.core.frame import DataFrame
from src.plots.strategies.plot_base import PlotBase
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

class BollingerBandADXRSIStrategyPlot(PlotBase):
            
    def filter_data(self, data, window, **args):
        data = data.iloc[-window:].copy()
        return data
    
    
    def plot_data(self, data: DataFrame, roll=7, **args) -> Figure:
        fig = plt.figure(figsize=(12, 5))  # Adjust the overall figure size as needed
        gs = gridspec.GridSpec(5, 1, height_ratios=[4,1,3,0.5,3])

        columns = [x for x in data.columns if x not in ['Open', 'High','Low','Adj Close','Volume']]
        columns_for_close = [x for x in columns if x not in ['rsi', f'ADX_{str(roll)}']]

        ax1 = plt.subplot(gs[0])
        for x in columns_for_close:
            ax1.plot(data[x], label=str(x)) 
            plt.xticks(data.index, rotation=90, ha='right', fontsize=6)
        ax1.legend(loc='upper left')

        ax2 = plt.subplot(gs[2])
        ax2.plot(data['rsi'], label=str('rsi'))
        ax2.axhline(70, color='red', linestyle='--', label='Reference Line at y=70')
        ax2.axhline(30, color='green', linestyle='--', label='Reference Line at y=30')
        ax2.legend(loc='upper left')

        ax3 = plt.subplot(gs[4])
        ax3.plot(data[f'ADX_{str(roll)}'], label=str(f'ADX_{str(roll)}'))
        ax3.axhline(25, color='green', linestyle='--', label='Reference Line at y=25')
        ax3.legend(loc='upper left')
        return fig