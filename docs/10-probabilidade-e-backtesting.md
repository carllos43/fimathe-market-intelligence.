# 10 — Probabilidade, taxa de acerto e backtesting

## Não confundir

- **Confiança qualitativa:** leitura subjetiva/estrutural, não é porcentagem estatística.
- **Probabilidade estimada:** previsão produzida por modelo calibrado.
- **Taxa de acerto histórica:** proporção de operações vencedoras em amostra definida.
- **Expectativa:** resultado médio por operação, incluindo perdas e custos.

## Métricas

- Win rate = operações vencedoras / operações encerradas.
- Loss rate = operações perdedoras / operações encerradas. Definir separadamente breakeven.
- Expectancy em R = média dos resultados líquidos em unidades de risco.
- Profit factor = lucro bruto / perda bruta.
- Max drawdown = maior queda do pico ao vale.
- MAE = máxima excursão adversa.
- MFE = máxima excursão favorável.
- Brier score/log loss para qualidade de probabilidades, quando houver previsão probabilística.

Win rate alto não significa estratégia lucrativa. Uma estratégia pode acertar muito e perder mais quando erra.

## Protocolo mínimo

1. Formalizar regras antes do teste.
2. Usar dados OHLC confiáveis e timestamps corretos.
3. Separar treino, validação e teste cronológico.
4. Evitar look-ahead bias e repainting.
5. Simular spread, comissão, slippage e swap.
6. Fazer walk-forward e testar em diferentes regimes.
7. Reportar número de trades, período, ativos e timeframes.
8. Apresentar intervalos de confiança e limitações.
9. Não otimizar parâmetros apenas para o passado.
10. Revalidar após mudanças de regra.

## Relato obrigatório

Nunca escrever “85% de chance” com base em impressão visual. Se não houver backtest aplicável, informar: “probabilidade estatística não disponível; leitura qualitativa apenas”.

Ao informar taxa histórica, indicar amostra, período, ativo(s), timeframe(s), custos e método. Não generalizar um resultado de EUR/USD H1 para todos os pares e timeframes.
