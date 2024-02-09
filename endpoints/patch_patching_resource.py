from utils.user_data import Users


class PatchingResource:

    def __init__(self, api):
        self.api = api

    def part_update_users(self):
        headers = {"Content-type": "application/json; charset=UTF-8"}
        data = {"title": f"{Users.title}"}

        response = self.api.patch(f'posts/{Users.id}', json=data, headers=headers)
        response_data = response.json()
        print(response_data)
        print(f"Получен ответ: {response_data} Статус код: {response.status_code}")

        assert response.status_code == 200, "Статус-код не соответствует ожидаемому"
        expected_keys = ["title", "body", "userId", "id"]
        for key in expected_keys:
            assert key in response_data, f"Ответ не содержит ожидаемый ключ: {key}"

        assert data["title"] == response_data[
            "title"], f"Значение 'title' в ответе '{response_data['title']}' не соответствует отправленному '{data['title']}'"
        return response
