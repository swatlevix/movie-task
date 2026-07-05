import requests

class ApiService:
    BASE_URL = "http://127.0.0.1:8000"

    def get(self, endpoint):
        response = requests.get(f"{self.BASE_URL}{endpoint}", timeout=10)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, data):
        response = requests.post(
            f"{self.BASE_URL}{endpoint}",
            json=data,
            timeout=10
        )
        response.raise_for_status()
        return response.json()