from requests import JSONDecodeError

from utils.user_data import Users


class DeletingResource:

    def __init__(self, api):
        self.api = api

    def delete_users(self):
        response = self.api.put(f'posts/{Users.id}')
        if response.status_code == 200:
            response_data = response.json()
            print(f"Получен ответ: {response_data} Статус код: {response.status_code}")
            assert response.status_code == 200, "Статус-код не соответствует ожидаемому"
        else:
            print(f"Ошибка: статус код {response.status_code}. Тело ответа: {response.text}")

        return response
