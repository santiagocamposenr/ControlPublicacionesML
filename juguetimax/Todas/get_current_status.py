from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery
#import logging
#logging.basicConfig(level=logging.INFO)

#logger = logging.getLogger(__name__)

def get_current_status(spreadsheet_id, range_):
    #logger.info('obtaining the current status')
    print('obtaining the current status')
    scope = 'https://www.googleapis.com/auth/spreadsheets.readonly'

    creds = ServiceAccountCredentials.from_json_keyfile_name('../creds.json', scope)

    service = discovery.build('sheets', 'v4', credentials=creds)

    sheet = service.spreadsheets()
    data = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_).execute()
    values = data['values']

    row_status = {}
    row = 1
    for value in values:
        if row == 1:
            row += 1
            continue
        else:
            row_status[row] = value[0].lower()
            row += 1
            continue
    
    return row_status

if __name__ == '__main__':
    spreadsheet_id = "1j0GvVT41xTc-mMLuyar2SEE7A3b8B8q4eItXdUhryz0"
    range_ = 'Todas!E:E'
    row_status = get__current_status(spreadsheet_id, range_)
    print(row_status)