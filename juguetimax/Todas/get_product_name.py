from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery
#import logging
#logging.basicConfig(level=logging.INFO)

#logger = logging.getLogger(__name__)

def get_todas_names():
    #print('obtaining names from todas')
    scope = 'https://www.googleapis.com/auth/spreadsheets.readonly'

    creds = ServiceAccountCredentials.from_json_keyfile_name('../creds.json', scope)

    service = discovery.build('sheets', 'v4', credentials=creds)

    spreadsheet_id = "1j0GvVT41xTc-mMLuyar2SEE7A3b8B8q4eItXdUhryz0"
    range_ = 'Todas!A:A'

    sheet = service.spreadsheets()
    data = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_).execute()
    values = data['values']

    names = {}
    row = 1
    for value in values:
        if row == 1:
            row += 1
            continue
        elif value == []:
            names[row] = value
            row += 1
            continue
        else:
            names[row] = value[0]
            row += 1
            continue

    return names


def get_activas_names():
    #print('obtaining names from activas')
    scope = 'https://www.googleapis.com/auth/spreadsheets.readonly'

    creds = ServiceAccountCredentials.from_json_keyfile_name('../creds.json', scope)

    service = discovery.build('sheets', 'v4', credentials=creds)

    spreadsheet_id = "1j0GvVT41xTc-mMLuyar2SEE7A3b8B8q4eItXdUhryz0"
    range_ = 'Activas!A:A'

    sheet = service.spreadsheets()
    data = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_).execute()
    values = data['values']

    names = {}
    row = 1
    for value in values:
        if row == 1:
            row += 1
            continue
        elif value == []:
            names[row] = value
            row += 1
            continue
        else:
            names[row] = value[0]
            row += 1
            continue

    return names


def get_pausadas_names():
    #print('obtaining names from pausadas')
    scope = 'https://www.googleapis.com/auth/spreadsheets.readonly'

    creds = ServiceAccountCredentials.from_json_keyfile_name('../creds.json', scope)

    service = discovery.build('sheets', 'v4', credentials=creds)

    spreadsheet_id = "1j0GvVT41xTc-mMLuyar2SEE7A3b8B8q4eItXdUhryz0"
    range_ = 'Pausadas!A:A'

    sheet = service.spreadsheets()
    data = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_).execute()
    values = data['values']

    names = {}
    row = 1
    for value in values:
        if row == 1:
            row += 1
            continue
        elif value == []:
            names[row] = value
            row += 1
            continue
        else:
            names[row] = value[0]
            row += 1
            continue

    return names


if __name__ == '__main__':
    todas = get_todas_names()
    print(todas)
    activas = get_activas_names()
    print(activas)
    pausadas = get_pausadas_names()
    print(pausadas)