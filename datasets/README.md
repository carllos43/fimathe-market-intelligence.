# Dados históricos e resultados de setups

O usuário não precisa fornecer esses dados para cada análise de imagem. A imagem enviada é a entrada da análise atual. Esta pasta é opcional e serve para armazenar histórico de operações/setup já encerrados, caso exista, permitindo medir resultados empíricos.

## Estrutura sugerida

```text
datasets/
  historical_setups.jsonl
  provider_name/
    EURUSD/
      M15.csv
      H1.csv
```

## Histórico de setups (JSONL)

Um objeto JSON por linha. Use `schemas/historical-setup.schema.json`. Campos essenciais:
- `instrument`, `timeframe`, `setup_type`, `market_regime`;
- `outcome`: `win`, `loss` ou `breakeven`;
- `costs_included`: spread, comissão, swap e slippage aplicáveis foram considerados;
- `out_of_sample`: o registro pertence a um período não usado para ajustar as regras;
- `rule_version`: versão da estratégia que gerou o registro;
- `closed_at`: data de encerramento.

Não inclua setups abertos ou resultados estimados. Não duplique operações. Registre também perdas e operações sem resultado positivo, sem selecionar apenas exemplos vencedores.

## Regras de uso

- O histórico é opcional. A análise visual funciona sem ele.
- Sem registros compatíveis, a IA deve dizer que não há probabilidade estatística disponível.
- Não misture timeframe, setup ou regime para inflar a amostra.
- A taxa validada exige no mínimo 50 operações comparáveis, custos incluídos e dados fora da amostra. O piso de 50 não substitui uma avaliação de robustez.
- Dados de terceiros só podem ser adicionados quando houver direito de uso. Não versionar credenciais ou dados privados.

## OHLC opcional

Para o motor Python, use CSV com `timestamp,open,high,low,close,volume`. Isso pode melhorar a precisão numérica, mas não é requisito para o usuário mandar uma imagem à IA.
