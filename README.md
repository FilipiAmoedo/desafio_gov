# Despesas Públicas Federais - Case de Estágio

Este projeto tem como objetivo acessar os dados de despesas públicas do governo federal por meio de uma API e visualizar esses dados em um dashboard no Power BI.

### Tecnologias Utilizadas
* Python: Para realizar a extração dos dados da API.
* Bibliotecas:
    * requests: Para realizar as requisições à API.
    * pandas: Para manipulação e tratamento dos dados.
* Power BI: Para criação de um dashboard interativo com os dados extraídos.
* API de Despesas Públicas do Governo Federal: Fonte dos dados utilizados.

  ### Estrutura do Projeto
  Dentro do package desafio_magalu o projeto esta estruturado dessa forma: 
    * API.py: Responsável por acessar a API e retornar os dados coletados.
    * E dentro de df_despesas_gov tem o arquivo df_recursos_recebidos.py que recebe os dados coletados pela API e converte-os em um arquivo Excel.
    * Re
  * dashboard.pbix: Arquivo do Power BI contendo o dashboard com visualizações das despesas públicas por órgão.
 
### Resultados
O dashboard no Power BI permite:
  * Visualizar o recebimento de recursos por órgão Superior.
  * Visualizar o recebimento de recursos por estado.
  * Identificar o máximo que uma entidade recebeu de recurso,total de recurso distribuido, pagamento de contas e o saldo líquido.
  * Clicando no ![image](https://github.com/user-attachments/assets/0ca2b2cc-3d6e-48de-bce5-2b6f05c14f21), podemos ver todas as informações citadas acima, porém segmentadas por estado, além de um gráfico que mostra o recebimento de recursos por órgão.
