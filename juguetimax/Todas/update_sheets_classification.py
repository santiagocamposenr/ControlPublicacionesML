from check_status_price import check_status_price
from move_sheets_registries import move_to_activas, move_to_pausadas
from make_dict_for_ml import make_dict_for_ml
from change_status_in_todas import change_status_in_todas

def update_sheets_classification(spreadsheet_id, range_for_links, range_for_status):
    print('updating sheets classification')

    rows_changed, rows_bad_links, rows_price = check_status_price(spreadsheet_id, range_for_links, range_for_status)

    dict_for_ml_changes = make_dict_for_ml(rows_changed, spreadsheet_id)

    #errors_in_ml_function = function_ml(dict_for_ml_changes)

    #if len(errors_in_ml_function) > 0:
        #for row in errors_in_ml_function:
            #rows_changed.pop(row)
    
    moves_to_activas = move_to_activas(rows_changed, rows_price, spreadsheet_id)

    moves_to_pausadas = move_to_pausadas(rows_changed, rows_price, spreadsheet_id)

    change_status_in_todas(moves_to_activas, moves_to_pausadas, spreadsheet_id)
    
    print('move to activas:\n')
    for row, value in moves_to_activas.items():
        print('row:', row, '\nid:', value[0], '\nproduct name:', value[1])

    print('move to pausadas:')
    for row, value in moves_to_pausadas.items():
        print('row:', row, '\nid:', value[0], '\nproduct name:', value[1])


if __name__ == '__main__':
    spreadsheet_id = "1j0GvVT41xTc-mMLuyar2SEE7A3b8B8q4eItXdUhryz0"
    range_for_links = 'Todas!C:C'
    range_for_status = 'Todas!E:E'

    update_sheets_classification(spreadsheet_id, range_for_links, range_for_status)
