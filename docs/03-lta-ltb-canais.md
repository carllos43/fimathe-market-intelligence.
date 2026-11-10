# 03 — LTA, LTB e canais

## LTA

Linha de tendência de alta conectando fundos ascendentes relevantes. Dois pontos permitem traçar uma linha; reações adicionais podem aumentar sua relevância, mas não garantem validade futura.

## LTB

Linha de tendência de baixa conectando topos descendentes relevantes.

## Critérios de construção automatizada

1. Usar pivôs confirmados.
2. Avaliar inclinação, distância entre pivôs e quantidade de toques.
3. Definir tolerância em unidades de volatilidade, como fração do ATR, em vez de tolerância fixa em pips para todos os ativos.
4. Penalizar linhas que atravessam muitos corpos de candles.
5. Distinguir toque, rejeição e rompimento.
6. Guardar a versão da linha e o momento em que ela se tornou conhecida.

## Canais

- Canal de alta: linha inferior ascendente e paralela superior projetada.
- Canal de baixa: linha superior descendente e paralela inferior projetada.
- Canal horizontal: limites de um range.
- Canal amplo/irregular: deve ser classificado como baixa qualidade, não forçado a caber no modelo.

## Rompimento de linha

Rompimento isolado não confirma reversão. Avaliar:
- fechamento além da linha;
- distância relativa ao ATR;
- quebra de swing estrutural;
- continuidade ou reteste;
- contexto do timeframe superior.

Uma linha pode ser redesenhada com novos pivôs, mas o histórico de versões precisa ser preservado para evitar viés retrospectivo.
