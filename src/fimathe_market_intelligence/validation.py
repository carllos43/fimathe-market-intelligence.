from .models import Candle

class DataValidationError(ValueError):
    pass

def validate_candles(candles):
    if not isinstance(candles, (list, tuple)) or len(candles) < 10:
        raise DataValidationError("Informe pelo menos 10 candles OHLC em ordem cronológica.")
    normalized = []
    previous_ts = None
    for i, item in enumerate(candles):
        c = item if isinstance(item, Candle) else Candle(**item)
        values = (c.open, c.high, c.low, c.close)
        if any(not isinstance(v, (int, float)) for v in values):
            raise DataValidationError(f"Candles[{i}]: OHLC precisa conter números.")
        if c.high < max(c.open, c.close, c.low) or c.low > min(c.open, c.close, c.high):
            raise DataValidationError(f"Candles[{i}]: relação OHLC inválida.")
        if c.high <= 0 or c.low <= 0:
            raise DataValidationError(f"Candles[{i}]: preços precisam ser positivos.")
        if c.timestamp and previous_ts and c.timestamp < previous_ts:
            raise DataValidationError("Candles devem estar em ordem cronológica.")
        if c.timestamp:
            previous_ts = c.timestamp
        normalized.append(c)
    return normalized
