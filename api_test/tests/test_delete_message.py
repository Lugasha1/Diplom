import allure


@allure.title("Тест на удаление сообщения")
def test_delete_message(headers, delete_message_endpoint, post_message_endpoint, get_message_endpoint):
    with allure.step("Отправка запроса на создание сообщения"):
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
    with allure.step("Отправка запроса на удаление сообщения"):
        delete_message_endpoint.delete_message(headers, message_id)
    with allure.step("Проверка статус кода"):
        delete_message_endpoint.check_status_code(204)
    with allure.step("Проверка, что сообщение не существует в канале"):
        get_message_endpoint.get_message_request(headers, message_id)
    with allure.step("Проверка статус кода"):
        get_message_endpoint.check_status_code(404)


@allure.title("Тест на удаление несуществующего сообщения")
def test_delete_non_exist_message(headers, delete_message_endpoint):
    with allure.step("Отправка запроса на удаление сообщения"):
        delete_message_endpoint.delete_message(headers, delete_message_endpoint.make_digit(5))
    with allure.step("Проверка статус кода"):
        delete_message_endpoint.check_status_code(404)


@allure.title("Тест на удаление сообщения без авторизации")
def test_delete_message_non_auth(headers_no_token, headers, post_message_endpoint, get_message_endpoint,
                                 delete_message_endpoint):
    with allure.step("Отправка запроса на создание сообщения"):
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
    with allure.step("Отправка запроса на удаление сообщения"):
        delete_message_endpoint.delete_message(headers, message_id)
    with allure.step("Проверка статус кода"):
        post_message_endpoint.check_status_code(401)