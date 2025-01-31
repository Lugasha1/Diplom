from dotenv import load_dotenv
import os
import random
import string
import pytest
import requests

# Загружаем переменные окружения из файла .env
load_dotenv()


class BaseEndpoint:
    def init(self):
        self.api_key = os.getenv("DISCORD_BOT_TOKEN")  # Загружаем токен из .env
        self.channel_id = int(os.getenv("CHANNEL_ID"))  # Загружаем ID канала из .env
        self.base_url = os.getenv("BASE_URL")  # Загружаем базовый URL из .env

        self.response_json = None
        self.response = None

    def get_request(self, url, headers):
        """Отправляет GET-запрос и возвращает JSON-ответ."""
        self.response = requests.get(url, headers=headers, verify=False)
        self.response_json = self.response.json()
        return self.response_json

    def post_request(self, url, headers, data):
        """Отправляет POST-запрос и возвращает JSON-ответ."""
        self.response = requests.post(url, headers=headers, data=data, verify=False)
        self.response_json = self.response.json()
        return self.response_json

    def delete_request(self, url, headers):
        """Отправляет DELETE-запрос."""
        self.response = requests.delete(url, headers=headers, verify=False)
        return self.response

    def check_status_code(self, code):
        """Проверяет, соответствует ли код ответа ожидаемому."""
        if self.response.status_code == code:
            pass
        else:
            pytest.fail(f'Error: {self.response.status_code}')

    def make_latin_lower(self, length):
        """Генерирует строку из случайных латинских строчных букв."""
        latin_lowercase_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
        return latin_lowercase_string

    def make_digit(self, length):
        """Генерирует строку из случайных цифр."""
        digit_string = ''.join(random.choice(string.digits) for _ in range(length))
        return digit_string