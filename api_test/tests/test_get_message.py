import allure


@allure.title("Тест на получение сообщения. Негативный. Неверный messageId")
def test_get_message_negative_not_found(get_message_endpoint, headers):
    with allure.step("Отправка запроса"):
        get_message_endpoint.get_message_request(headers, 123)
    with allure.step("Проверка статус кода"):
        get_message_endpoint.check_status_code(404)


@allure.title("Тест на получение сообщения. Негативный. Без авторизации")
def test_get_message_negative_no_auth(get_message_endpoint, headers_no_token):
    with allure.step("Отправка запроса"):
        get_message_endpoint.get_message_request(headers_no_token, 123)
    with allure.step("Проверка статус кода"):
        get_message_endpoint.check_status_code(401)