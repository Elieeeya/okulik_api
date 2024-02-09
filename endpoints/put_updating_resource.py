from requests import JSONDecodeError

from utils.user_data import Users


class UpdatingResource:

    def __init__(self, api):
        self.api = api

    def update_users(self):
        headers = {"Content-type": "application/json; charset=UTF-8"}
        data = {
            "title": f"{Users.title_ru}",
            "body": f"{Users.job_ru}",
            "userId": Users.id,
        }

        response = self.api.put(f'posts/{Users.id}', headers=headers, json=data)
        if response.status_code == 200:
            try:
                response_data = response.json()
                print(f"Получен ответ: {response_data} Статус код: {response.status_code}")
                assert response.status_code == 200, "Статус-код не соответствует ожидаемому"
                expected_keys = ["title", "body", "userId", "id"]
                for key in expected_keys:
                    assert key in response_data, f"Ответ не содержит ожидаемый ключ: {key}"

                assert data["title"] == response_data[
                    "title"], f"Значение 'title' в ответе '{response_data['title']}' не соответствует отправленному '{data['title']}'"
                assert data["body"] == response_data[
                    "body"], f"Значение 'body' в ответе '{response_data['body']}' не соответствует отправленному '{data['body']}'"
            except JSONDecodeError:

                print("Ответ не является валидным JSON.")
        else:
            print(f"Ошибка: статус код {response.status_code}. Тело ответа: {response.text}")

        return response
