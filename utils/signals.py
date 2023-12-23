def calculate_signal(historical_data, roll=7):
    close = historical_data.iloc[-1][ 'Close']
    adx = historical_data.iloc[-1][ f'ADX_{roll}']
    rsi = historical_data.iloc[-1][ 'rsi']
    bu = historical_data.iloc[-1][ f'BBU_{roll}_3.0']
    bl = historical_data.iloc[-1][ f'BBL_{roll}_3.0']
    bm = historical_data.iloc[-1][ f'BBM_{roll}_3.0']
    return close, adx, rsi, bu, bl, bm

def signals(historical_data, roll=7):
    close, adx, rsi, bu, bl, bm = calculate_signal(historical_data, roll)
    if (adx>25) and (rsi<30) and (close<bl):
        return 1
    else:
        return 0