from src.utils.generate_email import generate_emails

from src.models.model_catalog import Strategies
from config.parameters import Parameters

from data.instruments import symbols

def instantiate_strategy(symbols, strategy_name):
    try:
        params = Parameters[strategy_name.name].value
        generate_emails(symbols, strategy_name.value, **params)
    except ValueError:
        f"Unsupported strategy: {str(strategy_name)}"
    except Exception as e:
        print("Hit an exception", str(e))

def run():
    for strategy in Strategies:
        instantiate_strategy(symbols, strategy)


if __name__=="__main__":
    run()
    
    