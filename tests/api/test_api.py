import allure
import pytest
import requests


@pytest.mark.usefixtures("api")
class TestApi:
    @allure.epic("API Trainee")
    @allure.title("GET. Get User And Check Status Code")
    def test_get_single_user_and_check_status_code(self):
        uri = self.base_uri + "/api/users/2"
        response = requests.get(uri)
        assert response.status_code == 200

    @allure.epic("API Trainee")
    @allure.title("GET. Get User And Check Status Code")
    def test_get_single_user_and_check_name(self):
        expected_full_name = "Janet Weaver"
        uri = self.base_uri + "/api/users/2"
        response = requests.get(uri)
        response_body = response.json()
        first_name = response_body["data"]["first_name"]
        last_name = response_body["data"]["last_name"]
        full_name = f"{first_name} {last_name}"
        assert expected_full_name == full_name and response.status_code == 200

    @allure.epic("API Trainee")
    @allure.title("POST. Create a User")
    def test_post_create_user(self):
        uri = self.base_uri + "/api/users"
        name = "Morpheus"
        job = "Leader"
        body = {
            "name": name,
            "job": job
        }
        headers = "{'User-Agent': 'python-requests/2.26.0', " \
                  "'Accept-Encoding': 'gzip, deflate', 'Connection': 'keep-alive', " \
                  "'Content-Length': '24', 'Content-Type': 'application/x-www-form-urlencoded'}"
        response = requests.post(uri, body, headers)
        response_body = response.json()
        assert response.status_code == 201 and response_body["name"] == name and response_body["job"] == job

    @allure.epic("API Trainee")
    @allure.title("DELETE. Delete the User")
    def test_delete_user(self):
        uri = self.base_uri + "/api/users/2"
        response = requests.delete(uri)
        assert response.status_code == 204