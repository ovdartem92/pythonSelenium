import allure
import pytest
import requests


@pytest.mark.smoke
class TestApi:
    @allure.epic("Wildberries Trainee")
    @allure.title("API. Check Status Code")
    def test_get_locations_for_us_check_status_code_equals_200(self):
        response = requests.get("http://api.zippopotam.us/us/90210")
        assert response.status_code == 200

    @allure.epic("Wildberries Trainee")
    @allure.title("API. Check Country")
    def test_get_locations_for_us_check_country_equals_united_states(self):
        response = requests.get("http://api.zippopotam.us/us/90210")
        response_body = response.json()
        assert response_body["country"] == "United States"
