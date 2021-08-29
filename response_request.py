import requests

url = "https://kauth.kakao.com/oauth/token"

data = {
    "grant_type" : "authorization_code",
    "client_id" : "25e4c5fa84ea6248331959b692f7cb1b",
    "redirect_uri" : "https://localhost.com",
    "code" : "zcQVhFxqQibVu3ZuuWfnzNutXEiJVGzeKNzYrjnov6CINptk0s4L5jlFIfTSrRtAs5BLjwo9dJgAAAF7kF8QyA"
}

response = requests.post(url, data=data)

# 요청에 실패했다면
if response.status_code != 200:
    print("error! because ", response.json())
else:  # 성공했다면
    tokens = response.json()
    print(tokens)

# 발급받은 토큰은 유효기간이 있으며, 단 한번의 기회만 주어진다. 실패하거나 재시도하려면 다시 토큰을 발급받아야 함.
