def find_pivots(candles, left=3, right=3):
    highs, lows = [], []
    # Pivô só fica confirmado após os candles à direita fecharem.
    for i in range(left, len(candles)-right):
        h, l = candles[i].high, candles[i].low
        window = candles[i-left:i+right+1]
        if h == max(x.high for x in window) and sum(x.high == h for x in window) == 1:
            highs.append({"index": i, "price": h, "timestamp": candles[i].timestamp})
        if l == min(x.low for x in window) and sum(x.low == l for x in window) == 1:
            lows.append({"index": i, "price": l, "timestamp": candles[i].timestamp})
    return highs, lows

def classify_swings(highs, lows):
    result = []
    for kind, pivots in (("high", highs), ("low", lows)):
        for prev, cur in zip(pivots, pivots[1:]):
            label = ("HH" if cur["price"] > prev["price"] else "LH") if kind == "high" else ("HL" if cur["price"] > prev["price"] else "LL")
            result.append({"type": label, **cur})
    return sorted(result, key=lambda x: x["index"])

def classify_trend(highs, lows):
    if len(highs) < 2 or len(lows) < 2:
        return "unknown", "Estrutura insuficiente para classificar tendência."
    h_up, h_down = highs[-1]["price"] > highs[-2]["price"], highs[-1]["price"] < highs[-2]["price"]
    l_up, l_down = lows[-1]["price"] > lows[-2]["price"], lows[-1]["price"] < lows[-2]["price"]
    if h_up and l_up: return "up", "Últimos topos e fundos ascendentes (HH/HL)."
    if h_down and l_down: return "down", "Últimos topos e fundos descendentes (LH/LL)."
    if not h_up and not h_down and not l_up and not l_down: return "range", "Topos e fundos sem progressão direcional."
    return "mixed", "Topos e fundos não estão alinhados; possível transição ou lateralização."

def detect_break_of_structure(candles, highs, lows, atr_value, buffer_atr=0.1):
    last = candles[-1]
    buffer = atr_value * buffer_atr
    events = []
    if highs and last.close > highs[-1]["price"] + buffer:
        events.append({"type": "BOS", "direction": "bullish", "level": highs[-1]["price"], "confirmed_by_close": True})
    if lows and last.close < lows[-1]["price"] - buffer:
        events.append({"type": "BOS", "direction": "bearish", "level": lows[-1]["price"], "confirmed_by_close": True})
    return events
