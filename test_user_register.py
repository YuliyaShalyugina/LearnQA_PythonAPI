import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import pytest

class TestUserRegister(BaseCase):
    without_required_params = [
        ("username"),
        ("firstName"),
        ("lastName"),
        ("email"),
        ("password")
    ]

    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    def test_create_user_with_uncorrect_email(self):
        # email без символа @
        email = 'vinkotovexample.com'
        data = self.prepare_registration_data(email)

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == "Invalid email format", f"Unexpected response content {response.content}"

    @pytest.mark.parametrize('condition', without_required_params)
    def test_negative_create_user_without_required_param(self, condition):
        if condition == "username":
            data = self.prepare_registration_data_without_username()
        if condition == "firstName":
            data = self.prepare_registration_data_without_firstName()
        if condition == "lastName":
            data = self.prepare_registration_data_without_lastName()
        if condition == "email":
            data = self.prepare_registration_data_without_email()
        if condition == "password":
            data = self.prepare_registration_data_without_password()

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The following required params are missed: {condition}", \
            f"Unexpected response content {response.content}"


    def test_negative_create_user_with_param_firstName_1_character(self):
        data = self.prepare_registration_data_with_small_firstName()

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == "The value of 'firstName' field is too short", \
            f"Unexpected response content {response.content}"

    def test_negative_create_user_with_param_firstName_more_250_character(self):
        data = self.prepare_registration_data_with_firstName_more_250_character()

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == "The value of 'firstName' field is too long", \
            f"Unexpected response content {response.content}"
