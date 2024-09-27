# Desafio Estagio

* Para rodar o codigo, primeiro deve ir no arquivo env e no valor do dicionario botar sua chave para acessar a api 
            
        Exemplo : headers = {"chave-api-dados": "sua_chave_aqui"}

O codigo esta separado em 2 arquivos, sendo que em API temos a parte que so acessa a API e retorna os dados coletados, temos a função principal api_gov_despesas() e mais duas sendo elas a load_progress() e save_progress(page)

* A função save_progress(page) foi pensada para caso tenha alguma problema como queda de internet e tenha um erro a ultima pagina carregada esta salva dentro de um txt, podendo continuar de onde parou
* A função load_progress() caso tenha o arquivo ela apenas abre o txt e ve a ultima pagina feita para continuar dali, mas caso seja a primeira vez fazendo retorna 1 

O 2 arquivo é df_depesas_gov, onde pega os dados coletados da api e transforma em excel


! Quando eu coloquei para baixar os dados, acabou que ocorreu uma queda de internet e eu consegui acessar apenas 20751 paginas, acabei ficando com receio de colocar para baixar o resto e ficar com o tempo apertado para fazer,e como eu não tinha escrito um codigo para escrever os novos dados no excel já gerado, acabei optando por usar apenas os dados que foram gerados depois da queda 