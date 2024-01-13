import traceback
from src.utils.generate_email import generate_emails

from src.models.model_catalog import Strategies
from config.parameters import Parameters
from src.plots.plot_catalog import Plots

from data.instruments import symbols

def instantiate_strategy(symbols, strategy_name):
    try:
        params = Parameters[strategy_name.name].value
        plot_strategy = Plots[strategy_name.name].value 
        generate_emails(symbols, strategy_name.value, plot_strategy, **params)
    except ValueError:
        f"Unsupported strategy: {str(strategy_name)}"
    except Exception as e:
        print("Hit an exception", str(e))
        traceback.print_exc()

def run():
    for strategy in Strategies:
        instantiate_strategy(symbols, strategy)


if __name__=="__main__":
    run()
    
    