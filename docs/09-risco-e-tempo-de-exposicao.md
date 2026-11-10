# 09 — Risco e tempo de exposição

## Risco por operação

Definir risco monetário antes da entrada. O tamanho da posição depende da distância do stop, valor do pip/tick, moeda da conta e custos. Não recomendar alavancagem máxima.

## Custos

Incluir:
- spread variável;
- comissão;
- slippage;
- swap/financiamento overnight;
- gaps e execução;
- horário e liquidez da sessão.

## Quanto tempo ficar no mercado?

Não existe duração garantida derivada apenas do desenho do gráfico. A estimativa depende de timeframe, volatilidade, distância ao alvo, sessão e dados históricos.

A análise deve fornecer:
- horizonte provável em termos de candles (por exemplo, “a hipótese deve ser reavaliada nos próximos 3 a 5 candles” quando houver base);
- evento de saída por alvo;
- evento de saída por invalidação;
- limite temporal opcional (time stop), se definido pelo método;
- risco de manter posição durante notícias, rollover ou baixa liquidez.

Não transformar “até que hora” em horário exato sem dados de sessão, ativo, fuso e plano operacional. Em imagem estática, usar horizonte condicional, não previsão de relógio.
