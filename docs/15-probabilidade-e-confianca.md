# Probabilidade, confiança técnica e histórico

## Três medidas diferentes

1. **Pontuação de confluência (0–100):** resume quantos fatores técnicos definidos foram satisfeitos e qual parte dos fatores pôde ser avaliada. Não é chance de ganhar.
2. **Taxa histórica de acerto:** proporção de operações comparáveis que terminaram em ganho dentro de um conjunto de dados rotulado.
3. **Probabilidade futura calibrada:** estimativa validada em dados fora da amostra, com método documentado e custos considerados. É a única que pode ser apresentada como probabilidade estatística do setup, e mesmo assim não garante o próximo trade.

## Pontuação de confluência
O módulo `score_confluence` usa estes pesos iniciais:

| Fator | Peso |
|---|---:|
| Alinhamento com timeframe superior | 20 |
| Estrutura de mercado | 20 |
| Zona relevante | 15 |
| Gatilho de Price Action | 20 |
| Contexto de liquidez | 10 |
| R:R mínimo de 1,5 | 10 |
| Volatilidade adequada | 5 |

Fatores não avaliáveis são retirados do denominador e a cobertura é exibida. Uma pontuação alta significa apenas que mais condições técnicas foram satisfeitas. Os pesos são heurísticos e devem ser revisados após validação.

## Quando mostrar taxa histórica
Cada registro precisa ter, no mínimo:
- instrumento;
- timeframe;
- tipo de setup;
- regime de mercado;
- resultado (`win`, `loss` ou `breakeven`);
- custos incluídos;
- indicação de que pertence a teste fora da amostra;
- data e versão da regra usada.

O módulo `evaluate_historical_setups` exige correspondência exata de timeframe, setup e regime. Quando instrumento é informado, também exige o mesmo instrumento. Não mistura M15 com H1 nem setup de rompimento com setup de reversão.

A taxa só recebe `validated=true` quando todos os registros elegíveis têm custos incluídos, são fora da amostra e atingem pelo menos 50 operações. O tamanho mínimo é configurável e 50 é apenas um piso inicial, não garantia de robustez. O relatório inclui intervalo de Wilson de 95% para mostrar a incerteza amostral.

## O que não fazer
- Não converter 80 pontos de confluência em 80% de acerto.
- Não misturar registros de timeframes ou setups diferentes para aumentar a amostra.
- Não usar operações abertas, sem resultado, duplicadas ou com custos desconhecidos.
- Não selecionar parâmetros usando o mesmo período usado para medir o resultado final.
- Não apresentar taxa de acerto sem número de operações, período, instrumento/timeframe, custos e metodologia.

## Dados atuais insuficientes
Se não houver histórico rotulado e comparável, a resposta deve dizer: `Probabilidade estatística: indisponível — histórico comparável insuficiente.` A IA ainda pode apresentar a pontuação de confluência técnica, com a ressalva explícita de que não é taxa de acerto.
