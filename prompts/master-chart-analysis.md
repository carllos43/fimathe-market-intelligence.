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
1. Regime e direção dominante.
2. Últimos swings relevantes e sequência HH/HL ou LH/LL.
3. BOS/CHoCH: nível, candle de confirmação e se houve fechamento além do nível.
4. LTA/LTB/canal: pontos de ancoragem e quantidade de toques; marcar como hipótese quando houver poucos pontos.
5. Suportes, resistências, oferta/demanda e pools de liquidez.
6. Price Action recente e contexto do padrão.
7. Volatilidade visual e espaço disponível até o próximo obstáculo.
8. Conflitos entre direção maior e gatilho atual.

## Cenários
Compare:
- Compra: condição de ativação, entrada, stop, TP1, TP2, R:R e invalidação.
- Venda: condição de ativação, entrada, stop, TP1, TP2, R:R e invalidação.
- Espera: o que precisa acontecer para surgir uma entrada válida.

Escolha um cenário principal ou `AGUARDAR`. Uma entrada condicionada deve ser descrita como condicionada, não como ordem imediata. Não use o preço atual como entrada se o gatilho ainda não ocorreu.

## Horizonte
Use a faixa configurada para o timeframe. Informe quantidade de candles e equivalência aproximada em tempo corrido de mercado. Explique que é horizonte de reavaliação, não prazo garantido para TP.

## Probabilidade
Calcule a pontuação técnica de confluência usando os fatores disponíveis e mostre a cobertura. Consulte os registros históricos com correspondência de timeframe, tipo de setup e regime. Só mostre taxa histórica como validada se o conjunto atender aos critérios de `docs/15-probabilidade-e-confianca.md`. Se não atender, não converta pontuação em probabilidade.

## Formato final
Responda em português brasileiro, direto e específico. Use preços exatos apenas quando a escala permitir. Use a estrutura de `templates/analysis-report.md`. Não esconda incertezas nem force uma operação.
