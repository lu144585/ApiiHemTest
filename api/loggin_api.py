import requests
import app


class LoginApi:
    def __init__(self):
        self.login_url = app.HOST + "/api/sys/login"
        self.headers = app.HEADERS
    # 从外部接收mobile和password
    # 为什么这么写呢?这是因为，如果写成一个参数data
    def login(self, mobile, password):
        # 使用data来接收外部传入的mobilr和password,拼接成
        # 要发送的数据
        data = {
            "mobile": mobile,
            "password": password
        }
        response = requests.post(self.login_url,
                                 json=data,
                                 headers=self.headers)
        return response





































