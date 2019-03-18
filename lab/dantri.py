import requests
url= "https://dantri.com.vn/"
response = requests.get(url)
print(response.content.decode())