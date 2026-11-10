# Publicar como repositório GitHub separado

Nome do repositório: `fimathe-market-intelligence`.

1. No GitHub, crie um repositório vazio com esse nome.
2. Não marque para criar README, licença ou `.gitignore`, pois esses arquivos já estão neste pacote.
3. Extraia o ZIP. Abra o terminal dentro da pasta `fimathe-market-intelligence` e execute:

```bash
git init
git add .
git commit -m "feat: add market intelligence analysis engine"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/fimathe-market-intelligence.git
git push -u origin main
```

4. Troque `SEU_USUARIO` pelo seu usuário do GitHub.

## Verificação antes de publicar

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

Os testes cobrem validação OHLC, quantidade mínima de candles, saída sem probabilidade inventada e entrada vazia no módulo multi-timeframe.

Este pacote não cria o repositório remoto automaticamente. O conteúdo está pronto para ser enviado a um repositório novo; o repositório remoto precisa ser criado no GitHub primeiro.
