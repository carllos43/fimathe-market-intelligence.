# 02 — Estrutura de mercado

## 1. Swings

Um swing high é uma máxima local maior que as máximas de uma quantidade definida de candles à esquerda e à direita. Swing low é o equivalente para mínimas. Em tempo real, um pivô que depende de candles futuros ainda não está confirmado.

Defina `left_bars` e `right_bars`. Um pivô só deve ser marcado como confirmado depois de fechar o número necessário de candles à direita. Evite repainting: não apresente como conhecido no passado algo que só ficou visível depois.

## 2. Vocabulário

- HH (Higher High): topo mais alto que o topo de referência.
- HL (Higher Low): fundo mais alto que o fundo de referência.
- LH (Lower High): topo mais baixo que o topo de referência.
- LL (Lower Low): fundo mais baixo que o fundo de referência.

## 3. Classificação de regime

**Alta:** sequência estrutural predominante HH + HL. A hipótese de alta perde força se um fundo estrutural relevante for rompido com critério definido.

**Baixa:** sequência predominante LH + LL. A hipótese de baixa perde força se um topo estrutural relevante for rompido.

**Lateral:** ausência de progressão consistente; máximas e mínimas se mantêm dentro de limites ou os movimentos se sobrepõem.

**Transição/indefinido:** estrutura anterior foi danificada, mas a nova sequência ainda não foi estabelecida.

Não force o mercado a estar sempre em alta ou baixa. “Indefinido” é uma classificação válida.

## 4. BOS e CHoCH

Os termos variam entre escolas. Neste projeto:
- **BOS:** fechamento além de um swing relevante na direção da estrutura vigente, segundo a regra configurada.
- **CHoCH:** primeiro rompimento estrutural contrário à sequência vigente, tratado como alerta de possível mudança, não como reversão confirmada.
- **MSS:** usar apenas se o projeto definir critérios adicionais, como deslocamento, fechamento e quebra de swing protegido. Não usar como sinônimo universal de CHoCH.

## 5. Regras contra falsos sinais

- Preferir fechamento do candle ao simples toque ou pavio.
- Exigir que o nível rompido seja um swing previamente confirmado.
- Registrar a distância do fechamento ao nível e a amplitude média (por exemplo ATR).
- Classificar rompimentos sem continuidade como possíveis falhas.
- Não usar pivôs futuros para simular decisões passadas.

## 6. Força estrutural

Pode ser avaliada por:
- magnitude dos impulsos versus correções;
- distância percorrida por unidade de tempo;
- profundidade percentual da retração;
- frequência de rompimentos com continuidade;
- quantidade de swings confirmados na direção;
- alinhamento entre timeframes.

A pontuação deve ser calibrada com dados; não atribuir pesos arbitrários e chamar o resultado de probabilidade.
