import requests
import json

def request_ml(dict_for_ml_changes):
    # api-endpoint 
    # https://api.mercadolibre.com/oauth/token?grant_type=refresh_token&client_id=4137836578285892&client_secret=8F4UOJwVVxRGL2MV8LvS8zgDM0CnBfD1&refresh_token=TG-5ed69db9d50f750007f4a983-543440847
    url = "https://api.mercadolibre.com/oauth/token?"

    # sending get request and saving the response as response object
    params = {
        'grant_type': 'refresh_token',
        'client_id': '4137836578285892',
        'client_secret': '8F4UOJwVVxRGL2MV8LvS8zgDM0CnBfD1',
        'refresh_token': 'TG-5ed69db9d50f750007f4a983-543440847'
    }

    r = requests.post(url, data = params)

    # extracting data in json format 
    json_response = r.json()
    access_token = json_response['access_token']

    print('making requests to mercado libre')
    ## dict row : (id, status)
    url = "https://api.mercadolibre.com/items/"
    #Actualmente hay que agregar el token al correr el proyecto
    #access_token = "APP_USR-4137836578285892-060621-ca11da13828d48c95ee8996930dd6f10-543440847"
    header = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    errors_in_ml_function = []

    for row, value in dict_for_ml_changes.items():
        if value[1] == "activa":
            #https://api.mercadolibre.com/items/ITEM_ID?access_token=YOUR_ACCESS_TOKEN
            url_ = url + value[0] + "?access_token=" + access_token
            payload = {
                "status": "active"
            }
            r = requests.put(
                url_,
                headers=header,
                data=json.dumps(payload),
            )
            if r.status_code == 200:
                pass
            else:
                errors_in_ml_function.append(row)
        else:
            url_ = url + value[0] + "?access_token=" + access_token
            payload = {
                "status": "paused"
            }
            r = requests.put(
                url_,
                headers=header,
                data=json.dumps(payload),
            )
            if r.status_code == 200:
                pass
            else:
                errors_in_ml_function.append(row)

    return errors_in_ml_function