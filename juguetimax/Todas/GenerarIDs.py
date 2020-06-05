from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery
import re
#import logging
#logging.basicConfig(level=logging.INFO)

#logger = logging.getLogger(__name__)

def create_range(row, range_for_pub_links):
    parts = re.split('!', range_for_pub_links)
    part1 = parts[0]
    range_ = part1 + '!' + 'B' + str(row)
    return range_


def get_rows_ids(range_for_pub_ids):
    scope = 'https://www.googleapis.com/auth/spreadsheets.readonly'

    creds = ServiceAccountCredentials.from_json_keyfile_name('../creds.json', scope)

    service = discovery.build('sheets', 'v4', credentials=creds)

    sheet = service.spreadsheets()
    data = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_for_pub_ids).execute()
    values = data['values']
    
    number_rows = 0
    for value in values:
        number_rows += 1
        continue
        

    return number_rows


def generate_id(spreadsheet_id, range_for_pub_links, range_for_pub_ids):
    #logger.info('generating publication ids')
    print('generating publication ids')

    ids_rows = get_rows_ids(range_for_pub_ids)

    ## here we make sure we get authorize
    scope = 'https://www.googleapis.com/auth/spreadsheets'

    creds = ServiceAccountCredentials.from_json_keyfile_name('../creds.json', scope)

    service = discovery.build('sheets', 'v4', credentials=creds)

    ## here we read the sheet an extract the links of ML and extract the id
    sheet = service.spreadsheets()
    data = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_for_pub_links).execute()
    values = data['values']

    row = 1
    ids = {}
    for value in values:
        if row == 1:
            row += 1
            continue
        elif value == []:
            row += 1
            continue
        elif row < ids_rows:
            row += 1
            continue
        else:
            id_ = re.findall('MLM-[0-9]+', value[0])
            id_ = id_[0]
            id_ = id_.replace('-', '')
            ids[row] = id_    
            row += 1
            continue


    value_input_option = 'USER_ENTERED'
    insert_data_option = 'INSERT_ROWS'

    for row, value in ids.items():
        range_ = create_range(row, range_for_pub_links)
        value_range_body = {
                "range": range_,
                "majorDimension": 'ROWS',
                "values": [
                    [value]
                ]
                }

        sheet = service.spreadsheets()
        request = sheet.values().update(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, body=value_range_body)
        response = request.execute()

if __name__ == '__main__':
    spreadsheet_id = "1j0GvVT41xTc-mMLuyar2SEE7A3b8B8q4eItXdUhryz0"
    range_for_pub_links = "Todas!D:D"
    range_for_pub_ids = "Todas!B:B"
    generate_id(spreadsheet_id, range_for_pub_links, range_for_pub_ids)


