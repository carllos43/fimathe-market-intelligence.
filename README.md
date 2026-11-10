# Fimathe Market Intelligence

Sistema de referência para a IA analisar screenshots de gráficos Forex com Price Action, estrutura de mercado, cenários operacionais, horizonte por timeframe e validação histórica.

> **Escopo desta versão:** documentação técnica, regras conceituais, contrato de análise, esquema de dados e plano de validação. Este repositório não é, por si só, um robô operacional nem um sistema com taxa de acerto comprovada.

## Objetivo

O fluxo principal é **imagem enviada pelo usuário → leitura da IA → consulta às regras deste repositório → relatório operacional**. O usuário não precisa digitar OHLC, tendência, suportes ou indicadores. A IA interpreta o que estiver legível no screenshot e usa o motor OHLC quando houver candles estruturados disponíveis.

A resposta deve comparar compra, venda e espera e escolher o cenário mais defensável. Deve apresentar gatilho, entrada, stop, alvos, invalidação, risco/retorno e horizonte compatível com o timeframe. Se não houver gatilho claro, deve recomendar aguardar.

Leia primeiro `AI_INSTRUCTIONS.md`. Ele é o contrato principal para qualquer IA que use este repositório.

## Princípios obrigatórios

1. Não inventar preços, candles, níveis, horários ou dados ausentes.
2. Não declarar uma probabilidade numérica sem backtest reproduzível e amostra suficiente.
3. Diferenciar padrão em formação, confirmado e invalidado.
4. Não tratar rompimento de linha de tendência, candle isolado ou pavio como reversão automática.
5. Considerar spread, slippage, comissão, swap e horário do servidor quando calcular resultados.
6. Uma imagem estática não permite saber com precisão quando o preço atingirá um alvo nem quanto tempo uma operação ficará aberta.
7. Se o gráfico não mostrar ativo, timeframe, escala ou preço legível, declarar a limitação e solicitar os dados necessários.
8. Não emitir sinal quando a relação risco/retorno, a invalidação ou a estrutura não puderem ser definidas com clareza.

## Conteúdo

- `docs/01-fundamentos-price-action.md` — leitura de candles e comportamento do preço.
- `docs/02-estrutura-de-mercado.md` — tendência, swings, HH/HL/LH/LL, BOS e CHoCH.
- `docs/03-lta-ltb-canais.md` — linhas e canais de tendência.
- `docs/04-suporte-resistencia-zonas.md` — níveis, oferta e demanda.
- `docs/05-padroes-graficos-e-candles.md` — padrões de continuação, reversão e indecisão.
- `docs/06-liquidez-rompimentos-reteste.md` — falsos rompimentos, varreduras e retestes.
- `docs/07-contexto-multitimeframe.md` — alinhamento entre timeframes.
- `docs/08-projecoes-entrada-stop-alvos.md` — cenários, entrada, stop e take profit.
- `docs/09-risco-e-tempo-de-exposicao.md` — risco, custos e horizonte operacional.
- `docs/10-probabilidade-e-backtesting.md` — como medir acerto, erro e expectativa.
- `docs/11-protocolo-de-analise-de-imagem.md` — procedimento para analisar screenshots.
- `docs/12-glossario.md` — termos e definições operacionais.
- `docs/14-horizonte-por-timeframe.md` — faixa de candles e duração aproximada para reavaliação.
- `docs/15-probabilidade-e-confianca.md` — diferença entre pontuação técnica e taxa histórica validada.
- `AI_INSTRUCTIONS.md` — instrução principal para a IA analisar imagens.
- `prompts/master-chart-analysis.md` — procedimento e formato da leitura visual.
- `schemas/chart-observation.schema.json` — estrutura para dados extraídos da imagem.
- `schemas/historical-setup.schema.json` — estrutura para resultados históricos rotulados.
- `schemas/analysis-output.schema.json` — contrato JSON da resposta.
- `templates/analysis-report.md` — modelo de relatório.
- `datasets/README.md` — padrão para dados históricos.
- `tests/validation-checklist.md` — checklist de validação.

## Fluxo geral

```text
Imagem ou OHLC
    ↓
Verificação de qualidade e identificação do timeframe
    ↓
Detecção de swings e estrutura
    ↓
Classificação: alta / baixa / lateral / transição
    ↓
Zonas, LTA/LTB, canais, liquidez e padrões
    ↓
Leitura multi-timeframe (quando houver dados)
    ↓
Cenários condicionais e níveis de invalidação
    ↓
Entrada / stop / alvos / risco / horizonte estimado
    ↓
Backtest e calibração estatística (quando houver histórico)
    ↓
Relatório com fatos, hipóteses e incertezas separados
```

## Status de evidência

Use sempre uma destas etiquetas:
- **Observado:** diretamente visível no gráfico ou calculado a partir de OHLC fornecido.
- **Inferido:** interpretação coerente, mas ainda não confirmada.
- **Confirmado:** regra objetiva de confirmação foi satisfeita no fechamento do candle relevante.
- **Invalidado:** condição de invalidação foi atingida.
- **Não avaliável:** dados insuficientes.

## Aviso

Material educacional e de pesquisa. Não constitui recomendação financeira. Forex e CFDs podem envolver alavancagem e perdas superiores ao valor inicialmente esperado, conforme o produto e a jurisdição. Resultados históricos não garantem resultados futuros.

## Motor executável (versão 0.2)

O projeto inclui motor Python para dados OHLC, validação, ATR, pivôs, estrutura HH/HL/LH/LL, tendência, BOS simples, zonas, cenários, análise multi-timeframe, horizonte por timeframe, pontuação transparente de confluência e cálculo de estatística para setups históricos rotulados.

Consulte `INTEGRATION.md` para instalação e uso, `docs/13-arquitetura-do-motor.md` para arquitetura e `prompts/chart-image-extraction.md` para a camada de extração de screenshots.

**Limite importante:** o código Python não é, sozinho, um modelo de visão. A interpretação da imagem é feita pela IA que recebe o screenshot e segue `AI_INSTRUCTIONS.md`. O motor só deve receber OHLC extraído quando a leitura for confiável. Sem histórico comparável, rotulado, com custos e fora da amostra, a taxa estatística permanece indisponível. A pontuação técnica nunca deve ser apresentada como chance de acerto.
