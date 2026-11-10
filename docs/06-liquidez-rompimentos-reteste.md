# 06 — Liquidez, rompimentos e retestes

## Rompimento válido

Uma regra possível, que deve ser testada:
1. Identificar nível antes do evento.
2. Aguardar fechamento além da zona por margem mínima configurada.
3. Verificar deslocamento e contexto.
4. Avaliar continuidade ou reteste.
5. Invalidar se o preço fechar de volta na zona conforme regra definida.

## Falso rompimento / sweep

Preço ultrapassa uma máxima ou mínima observada e retorna para dentro da região. Isso pode representar falha de rompimento; não prova, isoladamente, que houve captura deliberada de ordens.

Registrar:
- nível varrido;
- profundidade da ultrapassagem;
- fechamento relativo ao nível;
- candle de retorno;
- estrutura subsequente;
- distância ao próximo nível.

## Reteste

Após romper uma região, o preço retorna para testá-la. O reteste pode:
- respeitar o nível e continuar;
- atravessar o nível e invalidar;
- ficar lateral e não oferecer entrada clara.

Não assumir que todo rompimento será retestado.

## Entrada por confirmação

O gatilho pode ser um fechamento, quebra de microestrutura ou rejeição definida. A entrada deve ocorrer somente depois do evento que a regra exige; não antecipar no backtest.
