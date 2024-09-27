import pandas as pd
from openpyxl import load_workbook
from desafio_magalu.api.api_gov import api_gov_despesas


def read_and_save(df):
    book = load_workbook('dados_coletados.xlsx')
    with pd.ExcelWriter('dados_coletados.xlsx', engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
        writer.book = book
        writer.sheets = {ws.title: ws for ws in book.worksheets}
        startrow = writer.sheets['Dados'].max_row
        df.to_excel(writer, startrow=startrow, index=False, header=False)

def save_excel():
    df = pd.DataFrame(api_gov_despesas())
    df.loc[df['siglaUFPessoa'] == '-1', 'siglaUFPessoa'] = 'Sem Informação'
    df.to_excel('dados_gov.xlsx', index=False)

if __name__ == '__main__':
    save_excel()