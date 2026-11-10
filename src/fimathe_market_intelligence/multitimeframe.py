from .analyzer import analyze_market

_ORDER = {"M1":1,"M5":5,"M15":15,"M30":30,"H1":60,"H2":120,"H4":240,"H8":480,"D1":1440,"W1":10080}

def analyze_multi_timeframe(data_by_timeframe, instrument=None):
    """Analyze each supplied timeframe independently and report directional confluence."""
    if not data_by_timeframe:
        raise ValueError("Informe candles para pelo menos um timeframe.")
    results = {}
    for timeframe, candles in sorted(data_by_timeframe.items(), key=lambda item: _ORDER.get(item[0].upper(), 10**9)):
        results[timeframe] = analyze_market(candles, instrument=instrument, timeframe=timeframe)
    directions = [r["trend"] for r in results.values() if r["trend"] in ("up", "down")]
    if directions and all(x == directions[0] for x in directions):
        confluence = "bullish" if directions[0] == "up" else "bearish"
    elif "up" in directions and "down" in directions:
        confluence = "conflicting"
    else:
        confluence = "mixed_or_insufficient"
    return {"instrument": instrument, "timeframes": results, "confluence": confluence,
            "limitations": ["Timeframes ausentes não foram inferidos.",
                            "Confluência é descritiva; não representa probabilidade de sucesso."]}
