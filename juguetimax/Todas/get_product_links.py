from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery
#import logging
#logging.basicConfig(level=logging.INFO)

#logger = logging.getLogger(__name__)

def get_links(spreadsheet_id, range_):
    #logger.info('obtaining the product´s links')
    print('obtaining the product´s links')
    scope = 'https://www.googleapis.com/auth/spreadsheets.readonly'

    creds = ServiceAccountCredentials.from_json_keyfile_name('../creds.json', scope)

    service = discovery.build('sheets', 'v4', credentials=creds)

    sheet = service.spreadsheets()
    data = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_).execute()
    values = data['values']

    row_link = {}
    row = 1
    for value in values:
        if row == 1:
            row += 1
            continue
        elif value == []:
            row_link[row] = value
            row += 1
            continue
        else:
            row_link[row] = value[0]
            row += 1
            continue
    
    return row_link
        

if __name__ == '__main__':
    spreadsheet_id = "1j0GvVT41xTc-mMLuyar2SEE7A3b8B8q4eItXdUhryz0"
    range_ = 'Todas!C:C'
    row_link = get_links(spreadsheet_id, range_)
    print(row_link)