import configuration
import requests
import data

def post_new_user(body):
    return requests.post(
                         configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body
                         )

def post_new_client_kit(kit_body, auth_token):
    str_token = "Barer " + auth_token
    heders_auth = data.headers["Authorization"] = str_token
    return requests.post(
                         configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=kit_body,
                         headers=data.headers
                        )
