# 08 — Projeções, entrada, stop e alvos

## Prioridade operacional: oportunidades locais

A partir da versão 0.3, o motor e a IA priorizam configurações próximas ao preço atual:

1. Analisar primeiro a janela recente (microestrutura).
2. Separar estrutura de contexto (range amplo / tendência maior) da estrutura de entrada (pivôs e zonas locais).
3. Aplicar filtro de distância operacional (`max_operational_distance_atr`). Se o stop ou gatilho estiver além do limite, o cenário é descartado e a análise é recalculada apenas na janela local.
4. Não utilizar automaticamente os extremos de um range amplo como entrada.
5. Calcular entrada, stop, TP1, TP2, distância em pips (quando o instrumento permitir), R:R e horizonte com base na estrutura local e no timeframe.
6. Comparar compra, venda e espera, escolhendo a configuração com melhor equilíbrio entre confirmação por fechamento, distância do stop e potencial de alvo.
7. Se não existir entrada válida próxima, retornar AGUARDAR e indicar exatamente o que precisa acontecer.

## Sempre apresentar cenários condicionais

- Cenário comprador.
- Cenário vendedor.
- Cenário neutro/espera.

O cenário principal deve ser o mais bem sustentado pelo gráfico, mas precisa de gatilho e invalidação explícitos.

## Entrada

A entrada pode ser:
- após fechamento de confirmação;
- no reteste confirmado;
- após quebra de microestrutura;
- em rejeição de zona com gatilho objetivo.

Informar se o preço indicado é uma região ou um preço exato. Em screenshot sem escala legível, não inventar cotação.

## Stop

O stop deve invalidar a hipótese técnica, não ser escolhido apenas para caber em uma relação risco/retorno desejada. Considerar:
- swing que sustenta o cenário;
- margem além da zona;
- ATR/volatilidade;
- spread e slippage;
- risco máximo por operação.

## Take profit

Possíveis referências:
- próximo swing;
- suporte/resistência;
- limite do canal;
- extensão de Fibonacci;
- projeção da amplitude do range;
- múltiplos de risco (R).

Apresentar alvos parciais quando houver níveis intermediários claros.

## Relação risco/retorno

R:R = distância da entrada ao alvo / distância da entrada ao stop, considerando direção e custos. Uma relação atraente não transforma uma operação ruim em boa.

## Invalidação

Especificar o evento exato: fechamento além do swing, perda da zona, rompimento contrário ou outro critério. Não usar frases vagas como “se o mercado mudar”.
