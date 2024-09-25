import requests
from core.headers import headers


def get_token(data):
    url = (
        "https://app.production.tonxdao.app/api/v1/login/web-app"
    )
    payload = {"initData":data}
    
    try:
        response = requests.post(url=url, headers=headers(), json=payload, timeout=20)
        data = response.json()
        token = data["access_token"]
        return token
    except:
        return None

