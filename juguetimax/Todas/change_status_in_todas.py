from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery

def create_range_for_todas(row):
    range_ = 'Todas!E' + str(row)
    return range_

def change_status_in_todas(moves_to_activas, moves_to_pausadas, spreadsheet_id):
    print('updating status in Todas')
    scope = 'https://www.googleapis.com/auth/spreadsheets'
    creds = ServiceAccountCredentials.from_json_keyfile_name('../creds.json', scope)
    service = discovery.build('sheets', 'v4', credentials=creds)

    value_input_option = 'USER_ENTERED'
    insert_data_option = 'INSERT_ROWS'

    for row in moves_to_activas.keys():
        range_ = create_range_for_todas(row)
        value_range_body = {
            "range": range_,
            "majorDimension": 'ROWS',
            "values": [
                ['activa']
            ]
            }

        sheet = service.spreadsheets()
        request = sheet.values().update(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, body=value_range_body)
        response = request.execute()

    for row in moves_to_pausadas.keys():
        range_ = create_range_for_todas(row)
        value_range_body = {
            "range": range_,
            "majorDimension": 'ROWS',
            "values": [
                ['pausada']
            ]
            }

        sheet = service.spreadsheets()
        request = sheet.values().update(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, body=value_range_body)
        response = request.execute()
