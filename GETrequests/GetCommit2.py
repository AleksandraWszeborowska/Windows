import jsonpath as jsonpath
import requests

# API url
url = "https://github.com/AleksandraWszeborowska/Windows"

# send Get Requests
response = requests.get(url)
print(response)

# display Response Content
print(response.content)
print(response.headers)