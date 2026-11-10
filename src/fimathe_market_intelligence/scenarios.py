def _pip_size(instrument):
    if not instrument:
        return None
    inst = instrument.upper().replace("/", "")
    return 0.01 if inst.endswith("JPY") else 0.0001

def _distance_ok(price_a, price_b, atr_value, max_atr):
    if atr_value <= 0:
        return True
    return abs(price_a - price_b) <= atr_value * max_atr

def _build_scenario(direction, entry, stop, target1, target2, trigger, invalidation, atr_value, config, instrument=None, local=True):
    risk = abs(entry - stop)
    if risk <= 0:
        return None
    if direction == "buy":
        reward1 = target1 - entry
        reward2 = target2 - entry
    else:
        reward1 = entry - target1
        reward2 = entry - target2
    if reward1 <= 0:
        return None
    rr = reward1 / risk
    if rr < config.min_risk_reward:
        return None
    if not _distance_ok(entry, stop, atr_value, config.max_operational_distance_atr):
        return None
    pip = _pip_size(instrument)
    def to_pips(d):
        return round(d / pip, 1) if pip else None
    return {
        "direction": direction,
        "trigger": trigger,
        "entry": round(entry, 8),
        "entry_type": "local_reference" if local else "context_reference",
        "entry_status": "wait_for_confirmation",
        "stop": round(stop, 8),
        "take_profit_1": round(target1, 8),
        "take_profit_2": round(target2, 8),
        "risk_pips": to_pips(risk),
        "reward1_pips": to_pips(reward1),
        "reward2_pips": to_pips(reward2),
        "risk_reward": round(rr, 2),
        "invalidation": invalidation,
        "horizon_candles": config.max_horizon_candles,
        "source": "local_microstructure" if local else "broader_context",
        "confidence_type": "qualitative",
        "probability": None,
    }

def make_scenarios(candles, trend, highs, lows, zones, atr_value, config, instrument=None):
    """Prioriza cenários baseados na microestrutura recente (próximos ao preço atual).
    Extremos de range amplo só entram como contexto, nunca como entrada padrão.
    """
    last = candles[-1]
    current = last.close
    buffer = atr_value * config.stop_buffer_atr
    scenarios = []

    # --- Análise local (janela recente) ---
    local_candles = candles[-config.local_lookback_candles:] if len(candles) > config.local_lookback_candles else candles
    local_highs, local_lows = [], []
    if len(local_candles) > config.local_pivot_left + config.local_pivot_right + 2:
        from .structure import find_pivots
        local_highs, local_lows = find_pivots(
            local_candles, config.local_pivot_left, config.local_pivot_right
        )
        # Ajustar índices relativos para absolutos se necessário (não crítico para preços)

    # Tentar construir cenário local de compra
    if local_lows:
        nearest_low = min(local_lows, key=lambda p: abs(p["price"] - current))
        if nearest_low["price"] < current and _distance_ok(current, nearest_low["price"], atr_value, config.max_operational_distance_atr):
            entry = current
            stop = nearest_low["price"] - buffer
            # Alvo local: próximo high local acima ou 2R
            local_res = next((h for h in reversed(local_highs) if h["price"] > current), None)
            target1 = local_res["price"] if local_res else entry + 2 * abs(entry - stop)
            target2 = entry + 3 * abs(entry - stop)
            sc = _build_scenario(
                "buy", entry, stop, target1, target2,
                "Microestrutura local: fundo recente próximo; considerar compra após confirmação por fechamento ou reteste do fundo local.",
                "Fechamento abaixo do fundo local usado no stop.",
                atr_value, config, instrument, local=True
            )
            if sc:
                scenarios.append(sc)

    # Tentar construir cenário local de venda
    if local_highs:
        nearest_high = min(local_highs, key=lambda p: abs(p["price"] - current))
        if nearest_high["price"] > current and _distance_ok(current, nearest_high["price"], atr_value, config.max_operational_distance_atr):
            entry = current
            stop = nearest_high["price"] + buffer
            local_sup = next((l for l in reversed(local_lows) if l["price"] < current), None)
            target1 = local_sup["price"] if local_sup else entry - 2 * abs(stop - entry)
            target2 = entry - 3 * abs(stop - entry)
            sc = _build_scenario(
                "sell", entry, stop, target1, target2,
                "Microestrutura local: topo recente próximo; considerar venda após confirmação por fechamento ou reteste do topo local.",
                "Fechamento acima do topo local usado no stop.",
                atr_value, config, instrument, local=True
            )
            if sc:
                scenarios.append(sc)

    # Filtro de distância operacional: descartar se ainda estiver muito longe
    scenarios = [s for s in scenarios if s is not None]

    # Se não houver cenário local válido, retornar espera (não forçar extremos do range amplo)
    if not scenarios:
        scenarios.append({
            "direction": "wait",
            "trigger": "Nenhuma configuração local válida próxima ao preço atual. Extremos de range amplo não são usados automaticamente como entrada.",
            "entry": None,
            "stop": None,
            "take_profit_1": None,
            "take_profit_2": None,
            "risk_reward": None,
            "invalidation": "Aguardar formação de microestrutura (pivô local confirmado) ou fechamento que defina gatilho próximo.",
            "horizon_candles": None,
            "source": "none",
            "confidence_type": "not_available",
            "probability": None,
            "reason": "Filtro de distância operacional: gatilhos distantes foram descartados em favor de oportunidades locais."
        })

    # Ordenar por melhor R:R entre os locais
    scenarios.sort(key=lambda s: s.get("risk_reward") or 0, reverse=True)
    return scenarios
