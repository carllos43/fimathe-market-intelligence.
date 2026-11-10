def make_scenarios(candles, trend, highs, lows, zones, atr_value, config):
    last = candles[-1]
    buffer = atr_value * config.stop_buffer_atr
    scenarios = []
    resistance = next((z for z in zones if z["kind"] == "resistance" and z["mid"] > last.close), None)
    support = next((z for z in zones if z["kind"] == "support" and z["mid"] < last.close), None)

    if trend == "up" and lows:
        entry = last.close
        stop = min(lows[-1]["price"], last.low) - buffer
        risk = entry-stop
        target = resistance["mid"] if resistance and resistance["mid"] > entry else entry + 2*risk
        rr = (target-entry)/risk if risk > 0 else None
        if rr and rr >= config.min_risk_reward:
            scenarios.append({"direction":"buy", "trigger":"Estrutura HH/HL; considerar compra somente após confirmação do gatilho no candle seguinte ou reteste sustentado.",
                "entry":round(entry, 8), "entry_type":"reference_price_not_active_order", "entry_status":"wait_for_confirmation", "stop":round(stop, 8), "take_profit_1":round(target, 8), "take_profit_2":round(entry+3*risk, 8),
                "risk_reward":round(rr, 2), "invalidation":"Fechamento abaixo do fundo estrutural usado no stop.", "horizon_candles":config.max_horizon_candles,
                "confidence_type":"qualitative", "probability":None})
    elif trend == "down" and highs:
        entry = last.close
        stop = max(highs[-1]["price"], last.high) + buffer
        risk = stop-entry
        target = support["mid"] if support and support["mid"] < entry else entry - 2*risk
        rr = (entry-target)/risk if risk > 0 else None
        if rr and rr >= config.min_risk_reward:
            scenarios.append({"direction":"sell", "trigger":"Estrutura LH/LL; considerar venda somente após confirmação do gatilho no candle seguinte ou reteste rejeitado.",
                "entry":round(entry, 8), "entry_type":"reference_price_not_active_order", "entry_status":"wait_for_confirmation", "stop":round(stop, 8), "take_profit_1":round(target, 8), "take_profit_2":round(entry-3*risk, 8),
                "risk_reward":round(rr, 2), "invalidation":"Fechamento acima do topo estrutural usado no stop.", "horizon_candles":config.max_horizon_candles,
                "confidence_type":"qualitative", "probability":None})
    if not scenarios:
        scenarios.append({"direction":"wait", "trigger":"Aguardar rompimento confirmado e reteste, ou nova sequência de pivôs que esclareça a estrutura.",
            "entry":None, "stop":None, "take_profit_1":None, "take_profit_2":None, "risk_reward":None,
            "invalidation":"Não há operação definida; reavaliar após fechamento de novos candles.", "horizon_candles":None,
            "confidence_type":"not_available", "probability":None})
    return scenarios
