import data
import sender_stand_request

# Добыча токена авторизации
def get_new_user_token():
    user_body = data.user_body.copy()
    response = sender_stand_request.post_new_user(user_body)
    auth_token = response.json()["authToken"]
    return auth_token

# Добыча тела запроса с подменой имени
def get_kit_body(name):
    kit = data.kit_body.copy()
    kit["name"] = name
    return kit

# Проверка, что корректные данные принимаются
def positive_assert(name):
    kit_response = get_kit_body(name)
    auth_token = get_new_user_token()
    kit_current_name = sender_stand_request.post_new_client_kit(kit_response, auth_token)
    assert kit_current_name.status_code == 201
    assert kit_current_name.json()["name"] == name

# Проверка, что некорректные данные  не принимаются
def negative_assert(name):
    kit_response = get_kit_body(name)
    auth_token = get_new_user_token()
    kit_current_name = sender_stand_request.post_new_client_kit(kit_response, auth_token)
    assert kit_current_name.status_code == 400
    assert kit_current_name.json()["code"] == 400

# Проверка, что запрос без параметра name  не будет выполнен
def negative_assert_no_name(name):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(name, auth_token)
    assert response.status_code == 400
    assert response.json()["code"] == 400

# Проверка, что можно создать набор с именем из 1 буквы
def test_create_kit_1_letter_in_name_get_success_response():
     positive_assert("А")

# Проверка, что можно создать набор с именем из 511 букв
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Проверка, что нельзя создать наор с пустым параметром name
def test_create_kit_empty_value_in_name_get_error_response():
    negative_assert("")

# Проверка, что нельзя создать набор с именем из 512 букв
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Проверка, что можно создать набор с именем из английских букв
def test_create_kit_english_letter_in_name_get_success_response():
    positive_assert("QWErty")

# Проверка, что можно создать набор с именем из русских букв
def test_create_kit_russian_letter_in_name_get_success_response():
    positive_assert("Мария")

# Проверка, что можно создать набор с именем из спецсимволов
def test_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert("\"№%@\",")

# Проверка, что можно создать набор с именем содержащим пробелы  букв
def test_create_kit_has_space_in_first_name_get_success_response():
    positive_assert("Человек и ко")

# Проверка, что можно создать набор с именем из цифр
def test_create_kit_has_number_in_first_name_get_success_response():
    positive_assert("123")

# Проверка, что нельзя создать набор с именем без параметра name
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_no_name(kit_body)

# Проверка, что нельзя создать набор с именем другого типа данных, нежели предусмотрены
def test_create_kit_number_type_name_get_error_response():
    kit_response = get_kit_body(123)
    auth_token = get_new_user_token()
    kit_current_name = sender_stand_request.post_new_client_kit(kit_response, auth_token)
    assert kit_current_name.status_code == 400
    assert kit_current_name.json()["code"] == 400