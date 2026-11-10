# Arquitetura do motor executável

A implementação inicial está em `src/fimathe_market_intelligence/`.

| Módulo | Responsabilidade |
|---|---|
| `validation.py` | Valida OHLC, preços positivos e ordem cronológica |
| `indicators.py` | True Range e ATR |
| `structure.py` | Pivôs confirmados, HH/HL/LH/LL, tendência e BOS |
| `zones.py` | Agrupa pivôs próximos em zonas de suporte/resistência |
| `scenarios.py` | Cenários condicionais, stop, alvos e relação risco/retorno |
| `analyzer.py` | Orquestra análise e monta saída JSON |
| `multitimeframe.py` | Analisa cada timeframe fornecido e mede alinhamento direcional |
| `cli.py` | Executa análise a partir de CSV |

## Fluxo de screenshot

O screenshot não deve ser convertido diretamente em preços inventados. A camada de visão deve devolver uma extração estruturada com:

- ativo e timeframe, ou `null` se não forem legíveis;
- OHLC apenas quando os valores estiverem disponíveis por fonte confiável ou extração visual com confiança suficiente;
- escala do eixo de preço e horário, se legíveis;
- indicação de candles cortados, indicadores que ocultem preços e baixa resolução;
- confiança por campo e coordenadas/regiões da imagem que sustentem a leitura.

Se a imagem não permitir recuperar OHLC com precisão, a IA pode produzir uma leitura visual qualitativa, mas não deve chamar o motor numérico nem inventar níveis exatos de entrada, stop ou alvo.

## Prompt-base para camada de visão

Ver `prompts/chart-image-extraction.md`. A camada de visão extrai evidências; não decide sozinha a operação. A decisão estruturada deve ser feita pelo motor e validada por regras.


## Priorização de oportunidades locais (v0.3)

O motor agora separa explicitamente:

- **Contexto maior**: pivôs e tendência calculados sobre todo o histórico fornecido.
- **Microestrutura local**: pivôs calculados apenas na janela recente (`local_lookback_candles`, padrão 40).

`scenarios.py` constrói primeiro cenários baseados nos pivôs locais próximos ao preço atual e aplica o filtro `max_operational_distance_atr`. Extremos distantes do range amplo não são usados como entrada operacional padrão. O campo `source` nos cenários indica `local_microstructure` ou `none`. O resultado inclui `operational_priority` e `primary_scenario`.

A IA deve seguir a mesma lógica ao interpretar imagens: priorizar candles recentes e não forçar entrada em extremos distantes.

A visão computacional e a interpretação do screenshot pertencem ao modelo de IA que recebe a imagem, não ao motor Python. O contrato de comportamento está em `AI_INSTRUCTIONS.md`; o procedimento está em `prompts/master-chart-analysis.md`; os campos extraídos estão em `schemas/chart-observation.schema.json`. A IA não deve exigir que o usuário transcreva OHLC quando consegue ler o gráfico. O motor Python é uma camada complementar para cálculos numéricos quando OHLC estiver disponível.

## Horizonte e evidência estatística

`horizon.py` centraliza faixas de reavaliação por timeframe. `statistics.py` separa pontuação de confluência de resultados históricos e calcula taxa empírica e intervalo de Wilson para registros comparáveis. A taxa só é marcada como validada com amostra mínima, custos incluídos e teste fora da amostra.
