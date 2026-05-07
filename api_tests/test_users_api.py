import requests


def test_get_users():

    headers = {
        "x-api-key": "free_user_3DOFvtmDCEbqESGHGCfdttmSNeS"
    }

    response = requests.get(
        "https://reqres.in/api/users?page=2",
        headers=headers
    )

    print(response.json())

    assert response.status_code == 200