from utils.user_data import Users


class CreatingResource:

    def __init__(self, api):
        self.api = api

    def new_users(self):
        data = {
            "title": f"{Users.title}",
            "body": f"{Users.job}",
            "userId": Users.id
        }

        response = self.api.post(f'posts', json=data)

        response_data = response.json()
        print(f"Получен ответ: {response_data} Статус код: {response.status_code}")

        assert response.status_code == 201, "Статус-код не соответствует ожидаемому"
        expected_keys = ["title", "body", "userId", "id"]
        for key in expected_keys:
            assert key in response_data, f"Ответ не содержит ожидаемый ключ: {key}"

        assert data["title"] == response_data[
            "title"], f"Значение 'title' в ответе '{response_data['title']}' не соответствует отправленному '{data['title']}'"
        assert data["body"] == response_data[
            "body"], f"Значение 'body' в ответе '{response_data['body']}' не соответствует отправленному '{data['body']}'"
        return response

