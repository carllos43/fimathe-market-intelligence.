# 08 — Projeções, entrada, stop e alvos

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
