import requests

print("Hello from Julia") #Ex3

#Ex4:
response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)

#response = requests.get("https://playground.learnqa.ru/api/hello")
#print(response.text)