import time

import allure
import pytest

import framework.utils.utils as utils
from framework.gmail_client.client import GmailClient

sender = "me"
to = "pythonseleniumovd@gmail.com"
expected_message_subject = utils.get_random_word()
expected_message_text = utils.get_random_word()
client = GmailClient()
service = client.authorize()


@pytest.mark.positive
@pytest.mark.api
class TestCheckGmailFunctionality:
    @allure.title("Check that all messages deleted in gmail")
    @allure.severity(severity_level="MINOR")
    def test_delete_all_messages(self):
        expected_count_of_message = 1
        client.delete_all_messages(service)
        message = client.create_message(sender, to, expected_message_subject, expected_message_text)
        client.send_message(service, message)
        actual_count_of_messages = client.get_count_of_messages(service)
        assert actual_count_of_messages == expected_count_of_message, \
            f"Expected count of message is {expected_count_of_message}, actual count of message is {actual_count_of_messages}"

    @allure.title("Check that body in email contains correctly data")
    @allure.severity(severity_level="MINOR")
    def test_send_message_and_check_it_body(self):
        message = client.create_message(sender, to, expected_message_subject, expected_message_text)
        message_id = client.send_message(service, message)
        time.sleep(1)
        actual_message = client.get_message_by_subject(service, expected_message_subject)
        client.delete_message_by_id(service, message_id)
        actual_message_text = actual_message["Message"]
        actual_message_subject = actual_message["Subject"]
        assert actual_message_text == expected_message_text, \
            f"Expected message is {expected_message_text}, actual message is {actual_message_text}"
        assert actual_message_subject == expected_message_subject, \
            f"Expected subject is {expected_message_subject}, actual subject is {actual_message_subject}"
