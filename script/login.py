import unittest, logging

import app
from api.loggin_api import LoginApi
from utils import assert_common


class Login(unittest.TestCase):
    def setUp(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        # 初始化登陆类
        cls.login_api = LoginApi()

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_login(self):
        # 调用封装登录接口
        response = self.login_api.login('13800000002', '123456')
        # 接收返回的json数据
        jsonData = response.json()
        # 调试出登录接口返回数据，日志输出只能作为{}占位符
        logging.info("登录接口返回数据:{}".format(jsonData))

        # 断言
        # self.assertEqual(200,response.status_code) #断言响应状态码
        # self.assertEqual(True,jsonData.get("success")) #断言success
        # self.assertEqual(10000,jsonData.get("code"))  #断言code
        # self.assertIn("操作成功",jsonData.get("message")) #断言message

        assert_common(self,
                      response,
                      200, True, 10000, '操作成功')

        token = jsonData.get("data")
        # 获取令牌，并拼接成以Bearer开头的令牌字符串
        app.HEADERS["Authorization"] = "Bearer " + token
        # 保存令牌到全局变量
        logging.info("保存的令牌是：{}".format(app.HEADERS))
