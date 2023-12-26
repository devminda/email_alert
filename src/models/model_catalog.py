from enum import Enum
from src.models.strategies.bb_adx_rsi_strategy import BollingerBandADXRSIStrategy


class Strategies(Enum):
    bollinger_band_adx_rsi = BollingerBandADXRSIStrategy

