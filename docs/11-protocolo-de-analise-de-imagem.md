# 11 — Protocolo de análise de screenshot

## Entrada

Extrair somente o que estiver visível:
- ativo/par;
- timeframe;
- corretora/plataforma, se legível;
- escala de preço;
- data/hora;
- candles completos;
- indicadores ou desenhos adicionados pelo usuário.

Se algum campo estiver ausente, marcar como desconhecido.

## Etapas

1. **Qualidade:** resolução, candles cortados, escala e legibilidade.
2. **Contexto:** regime e estrutura visíveis.
3. **Swings:** marcar pivôs confirmados e pivôs ainda provisórios.
4. **Geometria:** LTA/LTB, canais, range e padrões.
5. **Zonas:** suportes, resistências e regiões de reação.
6. **Comportamento:** impulsos, correções, rejeições, rompimentos e retestes.
7. **Cenários:** compra, venda e espera, cada um com gatilho e invalidação.
8. **Plano:** entrada, stop, alvos e R:R apenas se os preços puderem ser lidos.
9. **Tempo:** horizonte em candles ou condição de reavaliação; horário somente se houver base.
10. **Estatística:** somente métricas de backtest compatíveis com o setup.

## Quando não operar

- preço no meio de range sem vantagem clara;
- candles/escala ilegíveis;
- stop técnico indefinível;
- preço já muito distante do gatilho;
- relação risco/retorno insuficiente segundo regra definida;
- conflito relevante entre timeframes sem confirmação;
- notícia/evento de risco não avaliado;
- dados insuficientes.

## Formato da resposta

1. Ativo e timeframe.
2. Regime e tendência.
3. Estrutura HH/HL/LH/LL.
4. Zonas e linhas relevantes.
5. Price Action observado.
6. Cenário principal e alternativo.
7. Entrada (ou “aguardar”), stop, TP1/TP2.
8. R:R e condição de invalidação.
9. Horizonte/condição de saída.
10. Taxa histórica e probabilidade, ou declaração explícita de indisponibilidade.
11. Limitações da imagem.
