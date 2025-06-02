import requests
from locators.api_endpoints import REGISTER_ENDPOINT, DELETE_USER_ENDPOINT

def register_user(email, password, name):
    try:
        # на всякий случай пробуем удалить перед созданием
        delete_user_by_credentials(email, password)
    except Exception:
        pass
    response = requests.post(REGISTER_ENDPOINT, json={
        "email": email,
        "password": password,
        "name": name
    })
    response.raise_for_status()
    data = response.json()
    return data["accessToken"], data["refreshToken"]

def delete_user(access_token):
    headers = {"Authorization": access_token}
    response = requests.delete(DELETE_USER_ENDPOINT, headers=headers)
    response.raise_for_status()
    return response.json()

def delete_user_by_credentials(email, password):
    login_url = REGISTER_ENDPOINT.replace("register", "login")
    login_response = requests.post(login_url, json={"email": email, "password": password})
    login_response.raise_for_status()
    access_token = login_response.json()["accessToken"]
    return delete_user(access_token)