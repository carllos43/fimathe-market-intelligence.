def true_ranges(candles):
    out = []
    prev_close = None
    for c in candles:
        tr = c.high - c.low if prev_close is None else max(c.high-c.low, abs(c.high-prev_close), abs(c.low-prev_close))
        out.append(tr)
        prev_close = c.close
    return out

def atr(candles, period=14):
    trs = true_ranges(candles)
    if len(trs) < period:
        return sum(trs) / len(trs)
    # Média simples dos últimos N TRs: estável e reproduzível.
    return sum(trs[-period:]) / period
