import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
#print(response.history)
count_redirect = 0
for response in response.history:
        #print(response.url)
        count_redirect += 1
print(response.url)
print(count_redirect)