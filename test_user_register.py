from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import pytest
import allure
from allure import severity, severity_level

@allure.epic("Register user cases")
class TestUserRegister(BaseCase):
    without_required_params = [
        ("username"),
        ("firstName"),
        ("lastName"),
        ("email"),
        ("password")
    ]

    @severity(severity_level.CRITICAL)
    @allure.description("This test successfully create user")
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")


    @severity(severity_level.CRITICAL)
    @allure.description("This test trying to create user with existing email")
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"


    @severity(severity_level.NORMAL)
    @allure.description("This test trying to create user with invalid email format - without the @ symbol")
    def test_create_user_with_uncorrect_email(self):
        # email без символа @
        email = 'vinkotovexample.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == "Invalid email format", f"Unexpected response content {response.content}"


    @severity(severity_level.NORMAL)
    @pytest.mark.parametrize('condition', without_required_params)
    @allure.description("This test trying to create user without required params")
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

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The following required params are missed: {condition}", \
            f"Unexpected response content {response.content}"


    @severity(severity_level.NORMAL)
    @allure.description("This test trying to create user with firstName field is too short - 1 character")
    def test_negative_create_user_with_param_firstName_1_character(self):
        data = self.prepare_registration_data_with_small_firstName()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == "The value of 'firstName' field is too short", \
            f"Unexpected response content {response.content}"


    @severity(severity_level.NORMAL)
    @allure.description("This test trying to create user with firstName field more 250 character")
    def test_negative_create_user_with_param_firstName_more_250_character(self):
        data = self.prepare_registration_data_with_firstName_more_250_character()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == "The value of 'firstName' field is too long", \
            f"Unexpected response content {response.content}"
