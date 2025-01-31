import allure


@allure.title("Тест на отправку сообщения")
def test_post_message(headers, get_message_endpoint, post_message_endpoint):
    with allure.step("Отправка запроса"):
        data = {
            'content': post_message_endpoint.make_latin_lower(10)
        }
        post_message_endpoint.post_message_request(headers, data)
    with allure.step("Проверка статус кода"):
        post_message_endpoint.check_status_code(200)
    with allure.step("Получение id сообщения"):
        message_id = post_message_endpoint.get_message_id()
    with allure.step("Проверка, что сообщение существует в канале"):
        get_message_endpoint.get_message_request(headers, message_id)
    with allure.step("Проверка статус кода"):
        post_message_endpoint.check_status_code(200)


@allure.title("Тест на отправку сообщения. Негативный. Без тела запроса")
def test_post_message_empty_data(headers, post_message_endpoint):
    with allure.step("Отправка запроса"):
        data = {
        }
        post_message_endpoint.post_message_request(headers, data)
    with allure.step("Проверка статус кода"):
        post_message_endpoint.check_status_code(400)


@allure.title("Тест на отправку сообщения. Негативный. Без токена авторизации")
def test_post_message_empty_token(headers_no_token, post_message_endpoint):
    with allure.step("Отправка запроса"):
        data = {
            'content': post_message_endpoint.make_latin_lower(10)
        }
        post_message_endpoint.post_message_request(headers_no_token, data)
    with allure.step("Проверка статус кода"):
        post_message_endpoint.check_status_code(401)