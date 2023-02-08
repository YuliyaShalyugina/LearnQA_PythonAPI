import requests

response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print("GET, without param = method: ", response.text)

response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.status_code)
#print("HEAD, without param = method: ", response.text)

payload = {"method": "GET"}
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload)
print(response.status_code)
print("GET, with param = method: ", response.text)

#payload = {"method": "POST"}
#response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
#print(response.status_code)
#print("GET, with param = method: ", response.text)

mas = ["GET", "POST", "PUT", "DELETE"]
print(mas)
i = 0
for i in range (0, len(mas), 1):
    #print(mas[i])
    response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": mas[i]})
    print(f"get, with param = method:{mas[i]} ", response1.status_code)
    print(f"get, with param = method:{mas[i]} ", response1.text)

i = 0
for i in range (0, len(mas), 1):
    #print(mas[i])
    response2 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": mas[i]})
    print(f"post, with param = data:{mas[i]} ", response2.status_code)
    print(f"post, with param = data:{mas[i]} ", response2.text)

i = 0
for i in range (0, len(mas), 1):
    #print(mas[i])
    response3 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": mas[i]})
    print(f"put, with param = data:{mas[i]} ", response3.status_code)
    print(f"put, with param = data:{mas[i]} ", response3.text)

i = 0
for i in range (0, len(mas), 1):
    #print(mas[i])
    response4 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": mas[i]})
    print(f"delete, with param = data:{mas[i]} ", response4.status_code)
    print(f"delete, with param = data:{mas[i]} ", response4.text)