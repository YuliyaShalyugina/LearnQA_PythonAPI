import pytest
import requests

class TestNewFileUserAgent:
    user_agent_value = [
        ("1", "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"),
        ("2", "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"),
        ("3", "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"),
        ("4", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"),
        ("5", "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1")
    ]

    @pytest.mark.parametrize('num, params', user_agent_value)
    def test_user_agent_check(self, num, params):
        response = requests.get(
            "https://playground.learnqa.ru/ajax/api/user_agent_check",
            headers={"User-Agent": params}
        )
        #print("num = " , num)
        #print("params = ", params)
        platform = response.json()['platform']
        #print(platform)
        browser = response.json()['browser']
        #print(browser)
        device = response.json()['device']
        #print(device)

        if num == "1":
            print(num)
            assert platform == "Mobile", "Expected values 'platform' is not equal Mobile"
            assert browser == "No", "Expected values 'browser' is not equal No"
            assert device == "Android", "Expected values 'device' is not equal Android"
        elif num == "2":
            print(num)
            assert platform == "Mobile", "Expected values 'platform' is not equal Mobile"
            assert browser == "Chrome", "Expected values 'browser' is not equal Chrome"
            assert device == "iOS", "Expected values 'device' is not equal iOS"
        elif num == "3":
            print(num)
            assert platform == "Googlebot", "Expected values 'platform' is not equal Googlebot"
            assert browser == "Unknown", "Expected values 'browser' is not equal Unknown"
            assert device == "Unknown", "Expected values 'device' is not equal Unknown"
        elif num == "4":
            print(num)
            assert platform == "Web", "Expected values 'platform' is not equal Web"
            assert browser == "Chrome", "Expected values 'browser' is not equal Chrome"
            assert device == "No", "Expected values 'device' is not equal No"
        elif num == "5":
            print(num)
            assert platform == "Mobile", "Expected values 'platform' is not equal Mobile"
            assert browser == "No", "Expected values 'browser' is not equal No"
            assert device == "iPhone", "Expected values 'device' is not equal iPhone"
