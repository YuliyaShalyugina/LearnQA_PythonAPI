import requests

class TestNewFileCookie:
    def test_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        print(dict(response.cookies))

        cookie_value = response.cookies.get('HomeWork')
        assert cookie_value == "hw_value", "Cookie HomeWork is not equal hw_value"
