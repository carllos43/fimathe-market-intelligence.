# Prompt operacional — análise de gráfico por imagem

Aplique `AI_INSTRUCTIONS.md` e consulte os documentos deste repositório antes de concluir.

O usuário enviou uma imagem. Não solicite OHLC manualmente como primeira opção. Faça a leitura visual do gráfico e registre os campos abaixo com status `observed`, `estimated`, `uncertain` ou `not_visible`.

## Extração visual
- Instrumento/par: valor e confiança da leitura.
- Timeframe: valor e confiança da leitura.
- Plataforma/fonte: somente se visível.
- Preço atual e escala do eixo: valor, unidade e legibilidade.
- Candles visíveis: quantidade aproximada e janela temporal.
- Indicadores/linhas/zonas desenhadas: identificar sem presumir o significado se não houver legenda.
- Qualidade: resolução, corte, sobreposição, eixo legível e candles suficientes.

Não converta pixels em preços exatos sem escala legível e pontos de referência suficientes. Se necessário, apresente faixas aproximadas claramente identificadas como estimativas visuais.

## Leitura técnica
1. Regime de contexto e regime local (separados).
2. Microestrutura recente: últimos swings locais próximos ao preço atual.
3. BOS/CHoCH locais: nível, candle de confirmação e se houve fechamento além do nível.
4. LTA/LTB/canal apenas se ancorados na janela relevante.
5. Suportes, resistências e liquidez **locais** (próximos ao preço). Extremos de range amplo são contexto, não entrada padrão.
6. Price Action recente e confirmação por fechamento.
7. Filtro de distância operacional: se o gatilho/stop estiver além do limite (ATR ou range recente), descartar e reanalisar a janela local.
8. Volatilidade visual e espaço disponível até o próximo obstáculo local.

## Cenários
Compare:
- Compra local: condição de ativação próxima, entrada, stop local, TP1, TP2, R:R, pips e invalidação.
- Venda local: idem.
- Espera: o que precisa acontecer na microestrutura recente para surgir uma entrada válida próxima.

Escolha um cenário principal ou `AGUARDAR`. Uma entrada condicionada deve ser descrita como condicionada. Não use o preço atual como entrada se o gatilho ainda não ocorreu. Não force entrada em extremo distante.

## Horizonte
Use a faixa configurada para o timeframe. Informe quantidade de candles e equivalência aproximada em tempo corrido de mercado. Explique que é horizonte de reavaliação, não prazo garantido para TP.

## Probabilidade
Calcule a pontuação técnica de confluência usando os fatores disponíveis e mostre a cobertura. Consulte os registros históricos com correspondência de timeframe, tipo de setup e regime. Só mostre taxa histórica como validada se o conjunto atender aos critérios de `docs/15-probabilidade-e-confianca.md`. Se não atender, não converta pontuação em probabilidade.

## Formato final
Responda em português brasileiro, direto e específico. Use preços exatos apenas quando a escala permitir. Use a estrutura de `templates/analysis-report.md`. Não esconda incertezas nem force uma operação.
