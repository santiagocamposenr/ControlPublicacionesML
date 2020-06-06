import requests
import json

def request_ml(dict_for_ml_changes):
    ## dict row : (id, status)
    url = "https://api.mercadolibre.com/items/"
    #Actualmente hay que agregar el token al correr el proyecto
    access_token = ""
    header = {
        "Content-Type": "application/json",
        "Accept: application/json"
    }

    errors_in_ml_function = {}

    for row, value in dict_for_ml_changes.items():
        if value == "Activa":
            #https://api.mercadolibre.com/items/ITEM_ID?access_token=YOUR_ACCESS_TOKEN
            url_ = url + row + "?access_token" + access_token
            payload = {
                "status": "active"
            }
            r = requests.put(
                url_,
                headers=header,
                data=json.dumps(payload),
            )
            errors_in_ml_function[row] = r.status_code
        else:
            url_ = url + row + "?access_token" + access_token
            payload = {
                "status": "paused"
            }
            r = requests.put(
                url_,
                headers=header,
                data=json.dumps(payload),
            )
            errors_in_ml_function[row] = r.status_code
    return errors_in_ml_function