import jsonpath as jsonpath
import requests

# API url
url = "https://api.github.com/repos/AleksandraWszeborowska/Windows/commits/REF"

# send Get Requests
response = requests.get(url)
print(response)

# display Response Content
print(response.content)
print(response.headers)