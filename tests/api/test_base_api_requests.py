import allure
import pytest
import requests

import framework.utils.utils as utils


@pytest.mark.api
@pytest.mark.usefixtures("api")
class TestApi:
    @allure.epic("API Trainee")
    @allure.title("GET. Get User And Check Status Code")
    def test_get_single_user_and_check_status_code(self):
        expected_status_code = 200
        uri = self.base_uri + "/api/users/2"
        response = requests.get(uri)
        assert response.status_code == expected_status_code, \
            f"Expected status code is  {expected_status_code}, actual status code is {response.status_code}"

    @allure.epic("API Trainee")
    @allure.title("GET. Get User And Check Status Code")
    def test_get_single_user_and_check_name(self):
        expected_status_code = 200
        expected_full_name = "Janet Weaver"
        uri = self.base_uri + "/api/users/2"
        response = requests.get(uri)
        response_body = response.json()
        first_name = response_body["data"]["first_name"]
        last_name = response_body["data"]["last_name"]
        actual_full_name = f"{first_name} {last_name}"
        assert expected_full_name == actual_full_name and response.status_code == expected_status_code, \
            f"Expected status code is {expected_status_code}, actual status code is {response.status_code}" + \
            f"Expected full name {expected_full_name}, actual full name is {actual_full_name}"

    @allure.epic("API Trainee")
    @allure.title("POST. Create a User")
    def test_post_create_user(self):
        expected_status_code = 201
        uri = self.base_uri + "/api/users"
        name = utils.get_random_word()
        job = utils.get_random_word()
        body = {
            "name": name,
            "job": job
        }
        headers = "{'User-Agent': 'python-requests/2.26.0', " \
                  "'Accept-Encoding': 'gzip, deflate', 'Connection': 'keep-alive', " \
                  "'Content-Length': '24', 'Content-Type': 'application/x-www-form-urlencoded'}"
        response = requests.post(uri, body, headers)
        response_body = response.json()
        assert response.status_code == expected_status_code and response_body["name"] == name and response_body["job"] == job, \
            f"Expected status code is {expected_status_code}, actual status code is {response.status_code}"

    @allure.epic("API Trainee")
    @allure.title("DELETE. Delete the User")
    def test_delete_user(self):
        expected_status_code = 204
        uri = self.base_uri + "/api/users/2"
        response = requests.delete(uri)
        assert response.status_code == expected_status_code, \
            f"Expected status code is {expected_status_code}, actual status code is {response.status_code}"
