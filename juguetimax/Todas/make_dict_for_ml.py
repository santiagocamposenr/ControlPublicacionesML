from get_pub_ids import get_todas_ids 

def make_dict_for_ml(rows_changed_from_check_status_price_function, spreadsheet_id):
    print('making dictionary for ML')
    ## dict row : (id, status)
    dict_ = {}

    ids = get_todas_ids()

    for row, value in rows_changed_from_check_status_price_function.items():
        dict_[row] = (ids[row], value[1])
        continue

    return dict_
     