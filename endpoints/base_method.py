import requests


class Api:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, path, **kwargs):
        return requests.get(url=f"{self.base_url}{path}", **kwargs)

    def post(self, path, data=None, json=None, **kwargs):
        return requests.post(url=f"{self.base_url}{path}", data=data, json=json, **kwargs)

    def put(self, path, data=None, **kwargs):
        return requests.put(url=f"{self.base_url}{path}", data=data, **kwargs)

    def patch(self, path, data=None, **kwargs):
        return requests.patch(url=f"{self.base_url}{path}", data=data, **kwargs)

    def delete(self, path, **kwargs):
        return requests.delete(url=f"{self.base_url}{path}", **kwargs)
