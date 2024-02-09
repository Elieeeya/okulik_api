class GettingResource:
    def __init__(self, api):
        self.api = api

    def get_user(self):
        response = self.api.get('/posts/1')
        assert response.status_code == 200, "Статус-код не соответствует ожидаемому"
        data = response.json()

        required_keys = ['userId', 'id', 'title', 'body']
        for key in required_keys:
            assert key in data, f"Отсутствует ключ {key} в теле ответа"

        assert data['userId'] == 1, "Неверное значение userId"
        assert data['id'] == 1, "Неверное значение id"
        assert data['title'] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit", "Неверное значение title"
        assert data['body'].startswith("quia et suscipit"), "Тело сообщения не начинается с ожидаемого текста"

        return response
