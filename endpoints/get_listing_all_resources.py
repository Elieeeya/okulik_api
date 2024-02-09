class ListingAllResources:
    def __init__(self, api):
        self.api = api

    def get_all_users(self):
        response = self.api.get('posts')
        assert response.status_code == 200, "Статус-код не соответствует ожидаемому"
        data = response.json()

        expected_resource = {
            "userId": 1,
            "id": 1,
            "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
        }

        assert expected_resource in data, "Ожидаемый ресурс не найден в ответе"
        return response
