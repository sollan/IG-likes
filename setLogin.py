import json

login_data = {
    'username': '',
    'password': ''
}

with open("login.json","w") as f:
    json.dump(login_data, f)