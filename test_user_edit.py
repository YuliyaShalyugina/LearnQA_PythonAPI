from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure
from allure import severity, severity_level

@allure.epic("Edit user cases")
class TestUserEdit(BaseCase):
    @severity(severity_level.CRITICAL)
    @allure.description("This test successfully edit just created user")
    def test_edit_just_created_user(self):
        #REGISTER
        with allure.step("REGISTER USER"):
            register_data = self.prepare_registration_data()
            response1 = MyRequests.post("/user/", data=register_data)
        
            Assertions.assert_code_status(response1, 200)
            Assertions.assert_json_has_key(response1, "id")

            email = register_data['email']
            first_name = register_data['firstName']
            password = register_data['password']
            user_id = self.get_json_value(response1,"id")

        #LOGIN
        with allure.step("LOGIN USER"):
            login_data = {
                'email': email,
                'password': password
            }
            response2 = MyRequests.post("/user/login", data = login_data)

            auth_sid = self.get_cookie(response2, "auth_sid")
            token = self.get_header(response2, "x-csrf-token")

        #EDIT
        with allure.step("EDIT USER"):
            new_name = "Changed Neme"
            response3 = MyRequests.put(
                f"/user/{user_id}",
                headers={"x-csrf-token": token},
                cookies={"auth_sid": auth_sid},
                data={"firstName": new_name}
            )

            Assertions.assert_code_status(response3, 200)

        #GET
        with allure.step("GET USER"):
            response4 = MyRequests.get(
                f"/user/{user_id}",
                headers={"x-csrf-token": token},
                cookies={"auth_sid": auth_sid}
            )

            Assertions.assert_json_value_by_name(
                response4,
                "firstName",
                new_name,
                "Wrong name of the user after edit"
            )

    # Попытаемся изменить данные пользователя, будучи неавторизованными
    @severity(severity_level.CRITICAL)
    @allure.description("This test negative edit the user, being unauthorized")
    def test_edit_just_created_user_without_authorization(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # EDIT
        new_name = "Changed Neme"
        response2 = MyRequests.put(
            f"/user/{user_id}",
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response2, 400)
        assert response2.content.decode("utf-8") == "Auth token not supplied", \
            f"Unexpected response content {response2.content}"

    # Попытаемся изменить данные пользователя, будучи авторизованными другим пользователем
    @severity(severity_level.CRITICAL)
    @allure.description("This test negative edit the user, while being logged in by another user")
    def test_edit_just_created_user_with_authorization_other_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")
        #print(user_id)

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT OTHER USER
        new_name = "Changed Name"
        response3 = MyRequests.put(
            "/user/2",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )
        #print(response3.status_code)
        #print(response3.content)
        Assertions.assert_code_status(response3, 422)

        # GET
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response4, 200)
        print(response4.content)
        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            first_name,
            f"Wrong name of the user after edit other user. Expected : {first_name}. But Actual : {response4.json()['firstName']}"
        )

    # Попытаемся изменить email пользователя, будучи авторизованными тем же пользователем, на новый email без символа @
    @severity(severity_level.NORMAL)
    @allure.description("This test negative edit user's email, being authorized by the same user, to a new email without the @ symbol")
    def test_negative_edit_just_created_user_change_to_incorrect_email(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT
        new_email = "testExample.ru"
        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"email": new_email}
        )

        Assertions.assert_code_status(response3, 400)
        assert response3.content.decode("utf-8") == "Invalid email format", \
            f"Unexpected response content {response3.content}"

    # Попытаемся изменить firstName пользователя, будучи авторизованными тем же пользователем, на очень короткое значение в один символ
    @severity(severity_level.NORMAL)
    @allure.description("This test negative edit firstName, being authorized by the same user, to a very short value")
    def test_negative_edit_just_created_user_change_to_incorrect_firstName(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT
        new_firstName = "1"
        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_firstName}
        )

        Assertions.assert_code_status(response3, 400)
        assert response3.content.decode("utf-8") == '{"error":"Too short value for field firstName"}', \
            f"Unexpected response content {response3.content}"