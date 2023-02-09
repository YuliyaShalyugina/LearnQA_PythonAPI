import requests
import time

# Вызов метода без токена - метод заводит новую задачу
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
#print(response.status_code)
print("Without token: ", response.text)

parsed_response_text = response.json()
token_value = parsed_response_text["token"]
seconds_value = parsed_response_text["seconds"]
#print(token_value)

# Вызов метода c токеном ДО того, как задача готова + убеждался в правильности поля status
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":token_value})
#print("With token, expected status = Job is NOT ready : ", response.text)
parsed_response_text = response.json()
status_value = parsed_response_text["status"]
if status_value == "Job is NOT ready":
    print("Status is correct - ", status_value)
else:
    print(f"Expected status = Job is NOT ready, but actual status = {status_value}")

# Ожидание нужное количество секунд
time.sleep(seconds_value)

# Вызов метода c токеном ПОСЛЕ того, как задача готова + убеждался в правильности поля status
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":token_value})
parsed_response_text = response.json()
status_value = parsed_response_text["status"]
if status_value == "Job is ready":
    print("Status is correct - ", status_value)
else:
    print(f"Expected status = Job is ready, but actual status = {status_value}")