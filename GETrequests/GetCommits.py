import requests


def test_get_response_status_code():
    response = requests.get('https://api.github.com/repos/AleksandraWszeborowska/Windows')
    assert response.status_code == 200