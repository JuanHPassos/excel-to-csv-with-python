import csv
from googleapiclient.discovery import build

SPREADSHEET_ID = '1lXw184lTeepM7KMSYRFxcSSfkQgFfyifYbFRfOqDX4w'
RANGE_NAME = 'Dados'
API_KEY = ${{ secrets.NOME_DA_VARIAVEL }}

def authenticate_sheets(api_key):
    return build('sheets', 'v4', developerKey=api_key).spreadsheets()

def export_to_csv(data, filename='output.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

if __name__ == '__main__':
    sheets = authenticate_sheets(API_KEY)
    result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        export_to_csv(values)
        print('Data exported to output.csv')
