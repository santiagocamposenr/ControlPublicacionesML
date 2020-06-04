from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery
from get_pub_ids import get_todas_ids, get_activas_ids, get_pausadas_ids
from get_product_name import get_todas_names, get_activas_names, get_pausadas_names
#import logging
#logging.basicConfig(level=logging.INFO)

#logger = logging.getLogger(__name__)

def create_range_to_pausadas(row):
    range_ = 'Pausadas!' + str(row) + ':' + str(row)
    return range_

def create_range_to_activas(row):
    range_ = 'Activas!' + str(row) + ':' + str(row)
    return range_

def move_to_pausadas(rows_changed_from_check_status_price_function, rows_price, spreadsheet_id):
    print('moving to Pausadas')
    ## esta funcion te regresa un dict row_en_todas:(pub_id, product_name)
    moves = {}

    ## obtener nombres de producto y ids de publicacion
    names = get_todas_names()
    ids = get_todas_ids()

    for row, value in rows_changed_from_check_status_price_function.items():
        ## mover a pausadas
        if value[1] == 'pausada':
            ## obtener nombre de producto
            product_name = names[row]

            ## obtener id de publicacion
            publication_id = ids[row]

            ## ver si hay una fila vacia
            pausadas_ids = get_pausadas_ids()
            empty_rows = []
            for row_pausadas, value in pausadas_ids.items():
                if value == []:
                    empty_rows.append(row_pausadas)
                    continue
                else:
                    continue

            ## encontrar la fila en activas para traer los valores y eliminarla
            activas_ids = get_activas_ids()
            for row_activas, id in activas_ids.items():
                if publication_id == id:
                    row_to_clear = row_activas
                    break
                else:
                    continue
            
            try:
                if row_to_clear:
                    scope = 'https://www.googleapis.com/auth/spreadsheets.readonly'
                    creds = ServiceAccountCredentials.from_json_keyfile_name('../creds.json', scope)
                    service = discovery.build('sheets', 'v4', credentials=creds)
                    
                    range_ = range_ = 'Activas!' + str(row_to_clear) + ':' + str(row_to_clear)
                    sheet = service.spreadsheets()
                    data = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_).execute()
                    values = data['values']

                    data = values[0]

                    ## enviar la informacion a pausadas
                    ## insertar en fila vacia
                    if len(empty_rows) > 0:
                        ## here we make sure we get authorize
                        scope = 'https://www.googleapis.com/auth/spreadsheets'
                        creds = ServiceAccountCredentials.from_json_keyfile_name('../creds.json', scope)
                        service = discovery.build('sheets', 'v4', credentials=creds)

                        value_input_option = 'USER_ENTERED'
                        insert_data_option = 'INSERT_ROWS'
                        range_ = create_range_to_pausadas(empty_rows[0])
                        value_range_body = {
                            "range": range_,
                            "majorDimension": 'ROWS',
                            "values": [
                                data
                            ]
                            }

                        sheet = service.spreadsheets()
                        request = sheet.values().update(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, body=value_range_body)
                        response = request.execute()
                        
                        moves[row] = (publication_id, product_name)
                    
                    ## si no hay fila vacia
                    else:
                        ## here we make sure we get authorize
                        scope = 'https://www.googleapis.com/auth/spreadsheets'
                        creds = ServiceAccountCredentials.from_json_keyfile_name('../creds.json', scope)
                        service = discovery.build('sheets', 'v4', credentials=creds)

                        value_input_option = 'USER_ENTERED'
                        insert_data_option = 'INSERT_ROWS'
                        range_ = 'Pausadas'
                        value_range_body = {
                        "range": range_,
                        "majorDimension": 'ROWS',
                        "values": [
                            data
                        ]
                        }

                        sheet = service.spreadsheets()
                        request = sheet.values().append(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, insertDataOption=insert_data_option, body=value_range_body)
                        response = request.execute()

                        moves[row] = (publication_id, product_name)

                    ## eliminar registro de activas
                    scope = 'https://www.googleapis.com/auth/spreadsheets'
                    creds = ServiceAccountCredentials.from_json_keyfile_name('../creds.json', scope)
                    service = discovery.build('sheets', 'v4', credentials=creds)
                    
                    clear_values_request_body = {}
                    range_ = 'Activas!' + str(row_to_clear) + ':' + str(row_to_clear)

                    sheet = service.spreadsheets()
                    request = sheet.values().clear(spreadsheetId=spreadsheet_id, range=range_, body=clear_values_request_body)
                    response = request.execute()

            except:
                price = rows_price[row]

                ## insertar en fila vacia
                if len(empty_rows) > 0:
                    ## here we make sure we get authorize
                    scope = 'https://www.googleapis.com/auth/spreadsheets'
                    creds = ServiceAccountCredentials.from_json_keyfile_name('../creds.json', scope)
                    service = discovery.build('sheets', 'v4', credentials=creds)

                    value_input_option = 'USER_ENTERED'
                    insert_data_option = 'INSERT_ROWS'
                    range_ = create_range_to_pausadas(empty_rows[0])
                    value_range_body = {
                        "range": range_,
                        "majorDimension": 'ROWS',
                        "values": [
                            [product_name, publication_id, '', price]
                        ]
                        }

                    sheet = service.spreadsheets()
                    request = sheet.values().update(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, body=value_range_body)
                    response = request.execute()

                    moves[row] = (publication_id, product_name)
            
                ## si no hay fila vacia
                else:
                    ## here we make sure we get authorize
                    scope = 'https://www.googleapis.com/auth/spreadsheets'
                    creds = ServiceAccountCredentials.from_json_keyfile_name('../creds.json', scope)
                    service = discovery.build('sheets', 'v4', credentials=creds)

                    value_input_option = 'USER_ENTERED'
                    insert_data_option = 'INSERT_ROWS'
                    range_ = 'Pausadas'
                    value_range_body = {
                    "range": range_,
                    "majorDimension": 'ROWS',
                    "values": [
                        [product_name, publication_id, '', price]
                    ]
                    }

                    sheet = service.spreadsheets()
                    request = sheet.values().append(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, insertDataOption=insert_data_option, body=value_range_body)
                    response = request.execute()

                    moves[row] = (publication_id, product_name)

        else:
            pass
    
    return moves


def move_to_activas(rows_changed_from_check_status_price_function, rows_price, spreadsheet_id):
    print('moving to Activas')
    ## esta funcion te regresa un dict row_en_todas:(pub_id, product_name)
    moves = {}

    ## obtener nombres de producto y id de publicacion
    names = get_todas_names()
    ids = get_todas_ids()

    for row, value in rows_changed_from_check_status_price_function.items():
        ## mover a pausadas
        if value[1] == 'activa':
            ## obtener nombre de producto
            product_name = names[row]

            ## obtener id de publicacion
            publication_id = ids[row]

            ## ver si hay una fila vacia
            activas_ids = get_activas_ids()
            empty_rows = []
            for row_activas, value in activas_ids.items():
                if value == []:
                    empty_rows.append(row_activas)
                    continue
                else:
                    continue
            
            ## encontrar la fila de pausadas para traer los valores y para eliminarla 
            pausadas_ids = get_pausadas_ids()
            for row_pausadas, id in pausadas_ids.items():
                if publication_id == id:
                    row_to_clear = row_pausadas
                    break
                else:
                    continue
                
            try:
                if row_to_clear:
                    scope = 'https://www.googleapis.com/auth/spreadsheets.readonly'
                    creds = ServiceAccountCredentials.from_json_keyfile_name('../creds.json', scope)
                    service = discovery.build('sheets', 'v4', credentials=creds)
                    
                    range_ = range_ = 'Pausadas!' + str(row_to_clear) + ':' + str(row_to_clear)
                    sheet = service.spreadsheets()
                    data = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_).execute()
                    values = data['values']

                    data = values[0]

                    ## enviar la informacion a activas
                    ## insertar en fila vacia
                    if len(empty_rows) > 0:
                        ## here we make sure we get authorize
                        scope = 'https://www.googleapis.com/auth/spreadsheets'
                        creds = ServiceAccountCredentials.from_json_keyfile_name('../creds.json', scope)
                        service = discovery.build('sheets', 'v4', credentials=creds)

                        value_input_option = 'USER_ENTERED'
                        insert_data_option = 'INSERT_ROWS'
                        range_ = create_range_to_activas(empty_rows[0])
                        value_range_body = {
                            "range": range_,
                            "majorDimension": 'ROWS',
                            "values": [
                                data
                            ]
                            }

                        sheet = service.spreadsheets()
                        request = sheet.values().update(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, body=value_range_body)
                        response = request.execute()

                        moves[row] = (publication_id, product_name)
                    
                    ## si no hay fila vacia
                    else:
                        ## here we make sure we get authorize
                        scope = 'https://www.googleapis.com/auth/spreadsheets'
                        creds = ServiceAccountCredentials.from_json_keyfile_name('../creds.json', scope)
                        service = discovery.build('sheets', 'v4', credentials=creds)

                        value_input_option = 'USER_ENTERED'
                        insert_data_option = 'INSERT_ROWS'
                        range_ = 'Activas'
                        value_range_body = {
                        "range": range_,
                        "majorDimension": 'ROWS',
                        "values": [
                            data
                        ]
                        }

                        sheet = service.spreadsheets()
                        request = sheet.values().append(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, insertDataOption=insert_data_option, body=value_range_body)
                        response = request.execute()

                        moves[row] = (publication_id, product_name)

                    ## eliminar registro de pausadas
                    scope = 'https://www.googleapis.com/auth/spreadsheets'
                    creds = ServiceAccountCredentials.from_json_keyfile_name('../creds.json', scope)
                    service = discovery.build('sheets', 'v4', credentials=creds)
                    
                    clear_values_request_body = {}
                    range_ = 'Pausadas!' + str(row_to_clear) + ':' + str(row_to_clear)

                    sheet = service.spreadsheets()
                    request = sheet.values().clear(spreadsheetId=spreadsheet_id, range=range_, body=clear_values_request_body)
                    response = request.execute()

            except:
                price = rows_price[row]

                ## insertar en fila vacia
                if len(empty_rows) > 0:
                    ## here we make sure we get authorize
                    scope = 'https://www.googleapis.com/auth/spreadsheets'
                    creds = ServiceAccountCredentials.from_json_keyfile_name('../creds.json', scope)
                    service = discovery.build('sheets', 'v4', credentials=creds)

                    value_input_option = 'USER_ENTERED'
                    insert_data_option = 'INSERT_ROWS'
                    range_ = create_range_to_activas(empty_rows[0])
                    value_range_body = {
                        "range": range_,
                        "majorDimension": 'ROWS',
                        "values": [
                            [product_name, publication_id, '', price]
                        ]
                        }

                    sheet = service.spreadsheets()
                    request = sheet.values().update(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, body=value_range_body)
                    response = request.execute()

                    moves[row] = (publication_id, product_name)
            
                ## si no hay fila vacia
                else:
                    ## here we make sure we get authorize
                    scope = 'https://www.googleapis.com/auth/spreadsheets'
                    creds = ServiceAccountCredentials.from_json_keyfile_name('../creds.json', scope)
                    service = discovery.build('sheets', 'v4', credentials=creds)

                    value_input_option = 'USER_ENTERED'
                    insert_data_option = 'INSERT_ROWS'
                    range_ = 'Activas'
                    value_range_body = {
                    "range": range_,
                    "majorDimension": 'ROWS',
                    "values": [
                        [product_name, publication_id, '', price]
                    ]
                    }

                    sheet = service.spreadsheets()
                    request = sheet.values().append(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, insertDataOption=insert_data_option, body=value_range_body)
                    response = request.execute()

                    moves[row] = (publication_id, product_name)

        else:
            pass
    
    return moves