from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class Candle:
    timestamp: Optional[str]
    open: float
    high: float
    low: float
    close: float
    volume: Optional[float] = None

@dataclass(frozen=True)
class AnalysisConfig:
    pivot_left: int = 3
    pivot_right: int = 3
    atr_period: int = 14
    sr_tolerance_atr: float = 0.35
    breakout_buffer_atr: float = 0.10
    stop_buffer_atr: float = 0.20
    min_risk_reward: float = 1.5
    max_horizon_candles: int = 30
    # Priorização de oportunidades locais (próximas ao preço atual)
    local_lookback_candles: int = 40
    max_operational_distance_atr: float = 2.5
    local_pivot_left: int = 2
    local_pivot_right: int = 2
