# Checklist de validação

## Dados e imagem
- [ ] Ativo/timeframe identificados ou marcados como desconhecidos.
- [ ] Escala de preço legível antes de fornecer preços.
- [ ] Candles incompletos não foram tratados como fechados.
- [ ] Dados OHLC passam nas validações básicas.

## Estrutura
- [ ] Pivôs confirmados sem look-ahead.
- [ ] HH/HL/LH/LL comparados com swings relevantes.
- [ ] BOS/CHoCH usam regras documentadas.
- [ ] LTA/LTB usam pivôs conhecidos naquele instante.
- [ ] Range não foi forçado a virar tendência.

## Plano
- [ ] Entrada depende de gatilho explícito.
- [ ] Stop invalida a hipótese técnica.
- [ ] Alvos se apoiam em níveis/projeções observáveis.
- [ ] R:R inclui custos estimados.
- [ ] Cenário alternativo e condição de espera foram avaliados.
- [ ] Horizonte não é apresentado como horário garantido.

## Estatística
- [ ] Regras congeladas antes do teste.
- [ ] Separação cronológica treino/validação/teste.
- [ ] Sem repainting ou look-ahead.
- [ ] Custos e execução simulados.
- [ ] Amostra, período, ativo e timeframe reportados.
- [ ] Win rate não é confundido com expectativa.
- [ ] Probabilidade calibrada ou explicitamente indisponível.


## Validação do fluxo por imagem e estatística (v0.2)
- [ ] IA leu `AI_INSTRUCTIONS.md` antes de analisar a imagem.
- [ ] Ativo e timeframe foram extraídos apenas quando legíveis.
- [ ] Preços não legíveis não foram inventados.
- [ ] Compra, venda e espera foram comparadas.
- [ ] Entrada condicionada foi diferenciada de entrada imediata.
- [ ] Horizonte foi ajustado ao timeframe e descrito como reavaliação, não garantia.
- [ ] Pontuação técnica não foi chamada de probabilidade.
- [ ] Taxa histórica só foi exibida com amostra comparável, custos e teste fora da amostra.
- [ ] A resposta informou quando não havia dados suficientes.
