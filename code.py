import csv  # Biblioteca para manipulação de arquivos CSV
from googleapiclient.discovery import build  # Função para construir o serviço Google Sheets

# ID da planilha Google Sheets que será acessada
SPREADSHEET_ID = '1lXw184lTeepM7KMSYRFxcSSfkQgFfyifYbFRfOqDX4w'

# Nome da aba e intervalo de dados a serem recuperados(Pega tudo que foi preenchido)
RANGE_NAME = 'Dados'

# Chave de API do Google para autenticação no serviço Google Sheets(Variavel de ambiente)
API_KEY = ${{ secrets.API_KEY }}

# Função para autenticar e acessar a API do Google Sheets com a chave de API
def authenticate_sheets(api_key):
    # Retorna um serviço que permite acessar a planilha
    return build('sheets', 'v4', developerKey=api_key).spreadsheets()

# Função para exportar dados para um arquivo CSV
def export_to_csv(data, filename='output.csv'):
    # Abre ou cria o arquivo CSV com nome especificado (ou 'output.csv' por padrão)
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)  # Cria um escritor de CSV
        writer.writerows(data)  # Escreve todas as linhas de dados no CSV

# Código principal
if __name__ == '__main__':
    # Autentica e constrói o serviço do Google Sheets
    sheets = authenticate_sheets(API_KEY)
    
    # Busca valores no intervalo especificado da planilha
    result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    
    # Armazena os dados encontrados (ou uma lista vazia se não houver dados)
    values = result.get('values', [])

    # Verifica se não há dados
    if not values:
        print('No data found.')  # Informa que nenhum dado foi encontrado
    else:
        # Exporta os dados para um arquivo CSV
        export_to_csv(values)
        print('Data exported to output.csv')  # Informa que os dados foram exportados
