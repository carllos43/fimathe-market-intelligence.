"""Operational review horizons by chart timeframe.

These are configurable planning ranges, not predictions of how long price will take.
"""
from __future__ import annotations

TIMEFRAME_HORIZONS = {
    "M1": {"min_candles": 3, "max_candles": 15},
    "M5": {"min_candles": 3, "max_candles": 16},
    "M15": {"min_candles": 3, "max_candles": 12},
    "M30": {"min_candles": 3, "max_candles": 10},
    "H1": {"min_candles": 2, "max_candles": 12},
    "H4": {"min_candles": 2, "max_candles": 8},
    "D1": {"min_candles": 1, "max_candles": 8},
    "W1": {"min_candles": 1, "max_candles": 6},
}


def get_horizon(timeframe: str | None) -> dict:
    """Return a review horizon in candles and approximate clock duration."""
    if not timeframe:
        return {"timeframe": None, "min_candles": None, "max_candles": None,
                "min_duration": None, "max_duration": None,
                "status": "not_evaluable", "note": "Timeframe não identificado."}
    tf = timeframe.strip().upper()
    config = TIMEFRAME_HORIZONS.get(tf)
    if not config:
        return {"timeframe": tf, "min_candles": None, "max_candles": None,
                "min_duration": None, "max_duration": None,
                "status": "not_evaluable", "note": "Timeframe sem faixa configurada; não estimar duração."}
    minutes = {"M1": 1, "M5": 5, "M15": 15, "M30": 30,
               "H1": 60, "H4": 240, "D1": 1440, "W1": 10080}[tf]
    return {
        "timeframe": tf,
        "min_candles": config["min_candles"],
        "max_candles": config["max_candles"],
        "min_duration": _format_duration(config["min_candles"] * minutes),
        "max_duration": _format_duration(config["max_candles"] * minutes),
        "status": "planning_range",
        "note": "Faixa de reavaliação, não previsão nem prazo garantido para atingir o alvo."
    }


def _format_duration(total_minutes: int) -> str:
    if total_minutes < 60:
        return f"{total_minutes} min"
    if total_minutes < 1440:
        hours = total_minutes / 60
        return f"{hours:g} h"
    days = total_minutes / 1440
    return f"{days:g} dia(s)"
