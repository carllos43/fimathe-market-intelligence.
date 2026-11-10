# Integração do motor OHLC

## O que foi implementado

O pacote `src/fimathe_market_intelligence` contém uma primeira versão executável baseada em candles OHLC:

- validação de dados e ordem cronológica;
- cálculo de ATR;
- pivôs confirmados (aguardam `pivot_right` candles);
- classificação HH, HL, LH e LL;
- classificação de tendência por estrutura;
- detecção simples de BOS por fechamento;
- agrupamento de suporte e resistência por distância baseada no ATR;
- cenários condicionais de compra, venda ou espera, com stop, alvos e R:R quando há estrutura suficiente;
- saída JSON com probabilidade nula enquanto não existir backtest validado.

## Instalação local

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
fimathe-analyze examples/sample_ohlc.csv --instrument EURUSD --timeframe H1
```

Sem instalar o comando:

```bash
PYTHONPATH=src python -m fimathe_market_intelligence.cli examples/sample_ohlc.csv --instrument EURUSD --timeframe H1
```

## Integração em uma API

```python
from fimathe_market_intelligence import analyze_market

candles = [
    {"timestamp": "2026-01-01T10:00:00", "open": 1.10, "high": 1.12, "low": 1.09, "close": 1.11},
    # ... enviar pelo menos 10 candles, do mais antigo ao mais recente
]
result = analyze_market(candles, instrument="EURUSD", timeframe="H1")
```

## Limitações conhecidas desta primeira versão

1. O motor recebe OHLC; ele não interpreta screenshot diretamente. Para imagem, uma camada de visão deve extrair candles, escala, ativo e timeframe, e marcar cada campo como observado ou incerto antes de chamar este motor.
2. O algoritmo de pivôs é deliberadamente conservador e confirma pivôs apenas depois dos candles à direita. Isso evita usar informação futura na marcação do pivô, mas introduz atraso.
3. BOS é uma regra inicial por fechamento além do último pivô e buffer ATR. CHoCH, liquidez, padrões de candle, LTA/LTB e canais ainda precisam de módulos próprios e testes.
4. O cenário de entrada usa o fechamento atual como referência de preço, não uma ordem executável. A camada de execução deve aguardar o gatilho descrito e recalcular stop/alvos com spread e slippage.
5. Horizonte é um limite operacional de candles para reavaliação, não previsão de duração garantida.
6. Não existe taxa de acerto até integrar backtest com custos, separação treino/teste e amostra suficiente.

## Próxima integração recomendada

Conectar este pacote à API do produto, preservar a saída JSON, anexar dados de timeframe superior quando disponíveis e criar um módulo de backtest antes de exibir percentuais de probabilidade na interface.


## Fluxo por imagem (uso principal)

1. O usuário anexa o screenshot do gráfico na conversa com a IA.
2. A IA lê `AI_INSTRUCTIONS.md` e `prompts/master-chart-analysis.md`.
3. A IA extrai visualmente apenas os dados legíveis e marca incertezas. Não exige que o usuário transcreva OHLC.
4. A IA aplica a documentação de Price Action e entrega cenários de compra/venda/espera.
5. A IA usa `docs/14-horizonte-por-timeframe.md` para limitar a janela de reavaliação.
6. A IA consulta `datasets/` para setups históricos rotulados. Se não houver correspondência suficiente, informa que a probabilidade estatística está indisponível.

O relatório deve separar pontuação técnica de confluência e taxa histórica de acerto. Consulte `docs/15-probabilidade-e-confianca.md`.

## Novos módulos Python

```python
from fimathe_market_intelligence import get_horizon, score_confluence, evaluate_historical_setups

print(get_horizon("M15"))

score = score_confluence({
    "higher_timeframe_alignment": True,
    "market_structure": True,
    "key_zone": True,
    "price_action_trigger": False,
    "liquidity_context": None,
    "risk_reward_at_least_1_5": True,
    "volatility_suitable": None,
})

statistics = evaluate_historical_setups(
    records, timeframe="M15", setup_type="breakout_retest",
    market_regime="bullish", instrument="EURUSD"
)
```

`score_confluence` retorna uma pontuação técnica, não uma probabilidade. `evaluate_historical_setups` só marca a estatística como validada quando há pelo menos 50 registros comparáveis, todos fora da amostra e com custos incluídos.
