# Horizonte operacional por timeframe

Esta tabela define uma faixa inicial para planejar a reavaliação de um cenário. Não é previsão de duração, nem promessa de que o preço atingirá o alvo dentro da faixa.

| Timeframe | Reavaliar a partir de | Limite inicial | Equivalência aproximada |
|---|---:|---:|---|
| M1 | 3 candles | 15 candles | 3–15 minutos |
| M5 | 3 candles | 16 candles | 15–80 minutos |
| M15 | 3 candles | 12 candles | 45 minutos–3 horas |
| M30 | 3 candles | 10 candles | 1h30–5 horas |
| H1 | 2 candles | 12 candles | 2–12 horas |
| H4 | 2 candles | 8 candles | 8–32 horas |
| D1 | 1 candle | 8 candles | 1–8 dias de negociação |
| W1 | 1 candle | 6 candles | 1–6 semanas |

## Como aplicar
- O horizonte começa a contar depois da ativação do gatilho, não necessariamente no momento em que a imagem foi enviada.
- A faixa é um limite de planejamento e reavaliação. O preço pode atingir o alvo antes, não atingir ou invalidar o cenário imediatamente.
- Fechamento contra a estrutura, stop atingido, rompimento inválido ou perda do gatilho encerram a hipótese antes do limite máximo.
- Se a operação continuar válida ao chegar ao limite máximo, reavaliar estrutura, volatilidade, custos e proximidade do alvo. Não prolongar automaticamente.
- Para mercado fechado, feriados, gaps e sessões com baixa liquidez, a equivalência em relógio pode divergir do tempo real até o próximo candle.
- O timeframe menor não deve ser usado isoladamente para ampliar artificialmente o horizonte. O contexto maior só entra na análise se tiver sido fornecido.

Os valores estão centralizados em `src/fimathe_market_intelligence/horizon.py` para que o projeto mantenha uma única referência.
