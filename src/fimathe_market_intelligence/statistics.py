"""Historical outcome statistics for comparable, labeled setups.

A raw confluence score is deliberately not converted into a win probability.
Only out-of-sample records with costs included can be marked as validated.
"""
from __future__ import annotations
import math


def wilson_interval(wins: int, total: int, z: float = 1.96) -> tuple[float, float] | None:
    if total <= 0:
        return None
    p = wins / total
    denominator = 1 + z * z / total
    center = (p + z * z / (2 * total)) / denominator
    margin = (z * math.sqrt((p * (1 - p) / total) + (z * z / (4 * total * total)))) / denominator
    return max(0.0, center - margin), min(1.0, center + margin)


def evaluate_historical_setups(records, *, timeframe: str, setup_type: str,
                               market_regime: str, instrument: str | None = None,
                               min_sample_size: int = 50) -> dict:
    """Evaluate exact comparable records; no fuzzy matching or fabricated fallback.

    Each record must have outcome in {win, loss, breakeven}, matching setup/timeframe/
    regime, costs_included=true, and out_of_sample=true to qualify for validation.
    """
    eligible = []
    for record in records:
        if str(record.get("timeframe", "")).upper() != timeframe.upper():
            continue
        if record.get("setup_type") != setup_type or record.get("market_regime") != market_regime:
            continue
        if instrument and record.get("instrument") != instrument:
            continue
        if record.get("outcome") not in {"win", "loss", "breakeven"}:
            continue
        eligible.append(record)

    wins = sum(r["outcome"] == "win" for r in eligible)
    losses = sum(r["outcome"] == "loss" for r in eligible)
    breakeven = sum(r["outcome"] == "breakeven" for r in eligible)
    total = len(eligible)
    all_costs = bool(total) and all(r.get("costs_included") is True for r in eligible)
    all_oos = bool(total) and all(r.get("out_of_sample") is True for r in eligible)
    validated = total >= min_sample_size and all_costs and all_oos
    interval = wilson_interval(wins, total)
    return {
        "validated": validated,
        "win_rate": wins / total if total else None,
        "loss_rate": losses / total if total else None,
        "breakeven_rate": breakeven / total if total else None,
        "sample_size": total,
        "wins": wins, "losses": losses, "breakeven": breakeven,
        "confidence_interval_95": list(interval) if interval else None,
        "timeframe": timeframe.upper(), "setup_type": setup_type,
        "market_regime": market_regime, "instrument": instrument,
        "costs_included": all_costs,
        "out_of_sample": all_oos,
        "minimum_sample_size": min_sample_size,
        "methodology": "Frequência empírica de resultados rotulados em correspondência exata; intervalo de Wilson de 95%."
                      if total else "Nenhum registro histórico comparável encontrado.",
        "status": "validated" if validated else "insufficient_evidence"
    }


def score_confluence(factors: dict[str, bool | None]) -> dict:
    """Return a transparent technical confluence score, never a win probability."""
    weights = {
        "higher_timeframe_alignment": 20,
        "market_structure": 20,
        "key_zone": 15,
        "price_action_trigger": 20,
        "liquidity_context": 10,
        "risk_reward_at_least_1_5": 10,
        "volatility_suitable": 5,
    }
    available = {k: v for k, v in factors.items() if k in weights and v is not None}
    possible = sum(weights[k] for k in available)
    earned = sum(weights[k] for k, v in available.items() if v is True)
    score = round(100 * earned / possible) if possible else None
    return {
        "score": score,
        "label": "technical_confluence_score_not_win_probability",
        "factors": {k: {"passed": available[k], "weight": weights[k]} for k in available},
        "coverage": round(100 * possible / sum(weights.values())) if weights else 0,
        "warning": "Pontuação de confluência técnica. Não representa percentual de acerto nem probabilidade estatística."
    }
