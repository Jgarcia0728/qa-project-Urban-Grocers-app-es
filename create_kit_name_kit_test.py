import sender_stand_request
import data

# Función para cambiar el valor del parámetro name en el cuerpo de la solicitud
def get_kit_body(name):
    current_kit_body = data.kit_body.copy() # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    current_kit_body["name"] = name # Se cambia el valor del parámetro name
    return current_kit_body # Se devuelve un nuevo diccionario con el valor name requerido

def get_new_user_token(): # Función para cambiar el valor del parámetro name en el cuerpo de la solicitud
    user_body = data.user_body # El cuerpo de la solicitud actualizada se guarda en la variable
    response = sender_stand_request.post_new_user(user_body) # Llamamos la funcion
    return response.json()["authToken"]

def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body,get_new_user_token())
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body,get_new_user_token())
    assert response.status_code == 400

def test_1_create_kit_1_letter_in_the_name_success_response():
    current_kit_body = get_kit_body(data.test1_kit_name)
    positive_assert(current_kit_body)

def test_2_create_kit_511_letter_in_the_name_success_response():
    current_kit_body = get_kit_body(data.test2_kit_name)
    positive_assert(current_kit_body)

def test_3_create_kit_without_name():
    current_kit_body = get_kit_body(data.test3_kit_name)
    negative_assert_400(current_kit_body)

def test_4_create_kit_512_letter_in_the_name():
    current_kit_body = get_kit_body(data.test4_kit_name)
    negative_assert_400(current_kit_body)

def test_5_create_kit_symbol_in_the_name_success_response():
    current_kit_body = get_kit_body(data.test5_kit_name)
    positive_assert(current_kit_body)

def test_6_create_kit_space_in_letter_in_the_name_success_response():
    current_kit_body = get_kit_body(data.test6_kit_name)
    positive_assert(current_kit_body)

def test_7_create_kit_numbers_in_the_name_success_response():
    current_kit_body = get_kit_body(data.test7_kit_name)
    positive_assert(current_kit_body)

def test_8_create_kit_without_name_parameter():
    current_kit_body = data.kit_body.copy()
    current_kit_body.pop("name")
    negative_assert_400(current_kit_body)

def test_9_create_kit_parameter_numbers_in_name():
    current_kit_body = get_kit_body(data.test9_kit_name)
    negative_assert_400(current_kit_body)