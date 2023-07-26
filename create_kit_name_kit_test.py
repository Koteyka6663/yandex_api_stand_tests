import data
import sender_stand_request

def get_new_user_token():
    user_body = data.user_body.copy()
    response = sender_stand_request.post_new_user(user_body)
    auth_token = response.json()["authToken"]
    return auth_token

def get_kit_body(name):
    kit = data.kit_body.copy()
    kit["name"] = name
    kit_body = kit
    auth_token = get_new_user_token()
    kit_current_name = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    kit_current_name.json()["name"] = name
    return kit_current_name

def positive_assert(name):
    kit_response = get_kit_body(name)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name

def negative_assert(name):
    response = get_kit_body(name)
    assert response.status_code == 400
    assert response.json()["code"] == 400

def negative_assert_no_name(name):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(name, auth_token)
    assert response.status_code == 400
    assert response.json()["code"] == 400

def test_create_kit_1_letter_in_name_get_success_response():
     positive_assert("А")

def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def test_create_kit_empty_value_in_name_get_error_response():
    negative_assert("")

def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def test_create_kit_english_letter_in_name_get_success_response():
    positive_assert("QWErty")

def test_create_kit_russian_letter_in_name_get_success_response():
    positive_assert("Мария")

def test_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert("\"№%@\",")

def test_create_kit_has_space_in_first_name_get_success_response():
    positive_assert("Человек и ко")

def test_create_kit_has_number_in_first_name_get_success_response():
    positive_assert("123")

def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_no_name(kit_body)

def test_create_kit_number_type_name_get_error_response():
    kit_body = get_kit_body(123)
    response = kit_body
    assert response.status_code == 400
    assert response.json()["code"] == 400