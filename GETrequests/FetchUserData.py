import jsonpath as jsonpath
import requests

# API url
url = "https://reqres.in/api/users?page=2"

# send Get Requests
response = requests.get(url)
print(response)

# display Response Content
print(response.content)
print(response.headers)
