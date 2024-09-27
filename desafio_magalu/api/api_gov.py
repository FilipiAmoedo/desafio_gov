import requests
from desafio_magalu.env import headers
import time

URL = 'https://api.portaldatransparencia.gov.br/api-de-dados/despesas/recursos-recebidos'

PARAMS = {"mesAnoInicio": '05/2024',
          "mesAnoFim": '05/2024',
          "pagina": 1}


def save_progress(page):
    with open("last_page.txt", "w") as file:
        file.write(str(page))


def load_progress():
    try:
        with open("last_page.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 1


def api_gov_despesas():
    all_data = []
    pagina_atual = load_progress()  # Carrega a última página que foi salva no txt
    try:
        while True:
            response = requests.get(URL, headers=headers, params={"mesAnoInicio": '05/2024', "mesAnoFim": '05/2024', "pagina": pagina_atual})
            if response.status_code != 200:
                print(f"Erro: {response.status_code}")
                break
            data = response.json()
            if isinstance(data, list) and len(data) == 0:
                break
            all_data.extend(data)
            print(f"Página {pagina_atual} carregada.")
            pagina_atual += 1
            save_progress(pagina_atual)  # Salva a ultima pagina que foi feita em um txt
            time.sleep(1)  # Ajuste o tempo de espera entre requisições para não ultrapassar o limite
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        if all_data:  # Se já coletou alguns dados e ocorreu um erro, salva o progresso
            return all_data

    else:
        if all_data:  # Salva os dados se tudo correr bem
            return all_data


if __name__ == '__main__':
    api_gov_despesas()