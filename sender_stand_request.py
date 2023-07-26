import configuration
import requests
import data

# Создание нового пользователя
def post_new_user(body):
    return requests.post(
                            configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                            json=body,
                            headers=data.headers
                         )

# Создание набора пользователя
def post_new_client_kit(kit_body, auth_token):
    headers_dict = data.headers.copy()
    headers_dict["Authorization"] = "Bearer " + auth_token
    return requests.post(
                            configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                            json=kit_body,
                            headers=headers_dict
                        )
