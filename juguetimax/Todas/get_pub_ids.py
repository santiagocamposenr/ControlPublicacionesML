from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery
#import logging
#logging.basicConfig(level=logging.INFO)

#logger = logging.getLogger(__name__)

def get_todas_ids():
    #print('obtaining ids from todas')
    scope = 'https://www.googleapis.com/auth/spreadsheets.readonly'

    creds = ServiceAccountCredentials.from_json_keyfile_name('../creds.json', scope)

    service = discovery.build('sheets', 'v4', credentials=creds)

    spreadsheet_id = "1j0GvVT41xTc-mMLuyar2SEE7A3b8B8q4eItXdUhryz0"
    range_ = 'Todas!B:B'

    sheet = service.spreadsheets()
    data = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_).execute()
    values = data['values']

    ids = {}
    row = 1
    for value in values:
        if row == 1:
            row += 1
            continue
        elif value == []:
            ids[row] = value
            row += 1
            continue
        else:
            ids[row] = value[0]
            row += 1
            continue

    return ids


def get_activas_ids():
    #print('obtaining ids from activas')
    scope = 'https://www.googleapis.com/auth/spreadsheets.readonly'

    creds = ServiceAccountCredentials.from_json_keyfile_name('../creds.json', scope)

    service = discovery.build('sheets', 'v4', credentials=creds)

    spreadsheet_id = "1j0GvVT41xTc-mMLuyar2SEE7A3b8B8q4eItXdUhryz0"
    range_ = 'Activas!B:B'

    sheet = service.spreadsheets()
    data = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_).execute()
    values = data['values']

    ids = {}
    row = 1
    for value in values:
        if row == 1:
            row += 1
            continue
        elif value == []:
            ids[row] = value
            row += 1
            continue
        else:
            ids[row] = value[0]
            row += 1
            continue

    return ids


def get_pausadas_ids():
    #print('obtaining ids from pausadas')
    scope = 'https://www.googleapis.com/auth/spreadsheets.readonly'

    creds = ServiceAccountCredentials.from_json_keyfile_name('../creds.json', scope)

    service = discovery.build('sheets', 'v4', credentials=creds)

    spreadsheet_id = "1j0GvVT41xTc-mMLuyar2SEE7A3b8B8q4eItXdUhryz0"
    range_ = 'Pausadas!B:B'

    sheet = service.spreadsheets()
    data = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_).execute()
    values = data['values']

    ids = {}
    row = 1
    for value in values:
        if row == 1:
            row += 1
            continue
        elif value == []:
            ids[row] = value
            row += 1
            continue
        else:
            ids[row] = value[0]
            row += 1
            continue

    return ids


if __name__ == '__main__':
    todas = get_todas_ids()
    print(todas)
    activas = get_activas_ids()
    print(activas)
    pausadas = get_pausadas_ids()
    print(pausadas)