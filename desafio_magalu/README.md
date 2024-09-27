# Desafio de Estágio

Este projeto acessa dados de uma API e transforma-os em um arquivo Excel. Abaixo estão as instruções para execução do código.

### Como rodar o código

1. No arquivo `env`, insira sua chave de acesso à API no dicionário `headers`:
   ```python
   headers = {"chave-api-dados": "sua_chave_aqui"}

2. O código está dividido em dois arquivos:

* API.py: Responsável por acessar a API e retornar os dados coletados. Ele contém as seguintes funções:
      
  * api_gov_despesas(): Função principal para coletar os dados.
  * load_progress(): Carrega a última página processada a partir de um arquivo de texto, permitindo continuar a coleta de dados em caso de interrupções.
  * save_progress(page): Salva a página atual em um arquivo de texto, útil para retomar o processo após quedas de conexão ou erros.
* df_despesas_gov.py: Recebe os dados coletados pela API e converte-os em um arquivo Excel.
  
### Importante
Durante o processo de coleta, ocorreu uma queda de internet, e foram acessadas apenas 20.751 páginas. Por receio de perder tempo ajustando o restante, optei por trabalhar apenas com os dados obtidos até o momento. 