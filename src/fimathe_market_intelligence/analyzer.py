from dataclasses import asdict
from .models import AnalysisConfig
from .validation import validate_candles
from .indicators import atr
from .structure import find_pivots, classify_swings, classify_trend, detect_break_of_structure
from .zones import build_zones
from .scenarios import make_scenarios
from .horizon import get_horizon
from .statistics import score_confluence

def analyze_market(candles, instrument=None, timeframe=None, config=None):
    """Analyze chronological OHLC candles. This is a rule-based baseline, not an execution signal."""
    config = config or AnalysisConfig()
    candles = validate_candles(candles)
    atr_value = atr(candles, config.atr_period)
    highs, lows = find_pivots(candles, config.pivot_left, config.pivot_right)
    trend, trend_reason = classify_trend(highs, lows)
    current = candles[-1].close
    zones = build_zones(highs, lows, max(atr_value*config.sr_tolerance_atr, 1e-12), current)
    events = detect_break_of_structure(candles, highs, lows, atr_value, config.breakout_buffer_atr)
    scenarios = make_scenarios(candles, trend, highs, lows, zones, atr_value, config)
    horizon = get_horizon(timeframe)
    for scenario in scenarios:
        if scenario.get("direction") != "wait":
            scenario["horizon_candles"] = horizon["max_candles"]
    confidence = score_confluence({
        "higher_timeframe_alignment": None,
        "market_structure": trend in ("up", "down"),
        "key_zone": bool(zones),
        "price_action_trigger": None,
        "liquidity_context": None,
        "risk_reward_at_least_1_5": any((s.get("risk_reward") or 0) >= 1.5 for s in scenarios),
        "volatility_suitable": None,
    })
    regime = {"up":"bullish", "down":"bearish", "range":"sideways", "mixed":"transition"}.get(trend, "unknown")
    evidence = "confirmed" if events else ("inferred" if trend in ("up", "down", "range", "mixed") else "not_evaluable")
    swings = classify_swings(highs, lows)
    return {
        "instrument": instrument, "timeframe": timeframe,
        "chart_timestamp": candles[-1].timestamp,
        "market_regime": regime, "trend": trend, "trend_reason": trend_reason,
        "evidence_status": evidence,
        "structure": {"swings": [{"type":s["type"], "price":s["price"], "confirmed_at":s["timestamp"]} for s in swings],
                      "bos_events": events,
                      "latest_confirmed_swing_high": highs[-1] if highs else None,
                      "latest_confirmed_swing_low": lows[-1] if lows else None},
        "zones": [{k:z[k] for k in ("kind","low","high","mid","touches","distance")} for z in zones[:12]],
        "volatility": {"atr": round(atr_value, 8), "atr_period": config.atr_period},
        "scenarios": scenarios,
        "horizon": horizon,
        "technical_confluence": confidence,
        "statistics": {"validated": False, "win_rate": None, "loss_rate": None, "sample_size": None,
                       "period": None, "assets_timeframes": [], "costs_included": False,
                       "methodology": "Sem backtest conectado. Nenhuma taxa de acerto/erro é estimada."},
        "limitations": ["Análise baseada apenas nos candles OHLC enviados.",
                        "Não há contexto de timeframes superiores sem dados adicionais.",
                        "Probabilidades estatísticas indisponíveis até existir backtest fora da amostra.",
                        "Entrada sugerida é referência de cenário; exigir confirmação e considerar spread/slippage."]
    }
