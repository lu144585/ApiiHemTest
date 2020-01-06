import unittest,logging
from api.loggin_api import LoginApi
from utils import assert_common


class TestIHRMLogin(unittest.TestCase):
    def setUp(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        # 初始化登陆类
        cls.login_api=LoginApi()


    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass


    def test01_login_success(self):
        # 调用封装登录接口
        response=self.login_api.login('13800000002','123456')
       #接收返回的json数据
        jsonData=response.json()
        # 调试出登录接口返回数据，日志输出只能作为{}占位符
        logging.info("登录接口返回数据:{}".format(jsonData))

        # 断言
        # self.assertEqual(200,response.status_code) #断言响应状态码
        # self.assertEqual(True,jsonData.get("success")) #断言success
        # self.assertEqual(10000,jsonData.get("code"))  #断言code
        # self.assertIn("操作成功",jsonData.get("message")) #断言message

        assert_common(self,
                      response,
                      200,True,10000,'操作成功')



    def test02_username_is_not_exist(self):
        # 调用封装的登录接口
        response=self.login_api.login('13900000002','123456')
        # 接收返回的json数据
        jsonData=response.json()
#         输出
        logging.info("账号存在时输出数据：{}".format(jsonData))
#         断言
        assert_common(self,response,200,False,20001,"用户名或密码错误")


    def test03_password_is_not_exist(self):
#         调用封装的登录接口
        response=self.login_api.login('13800000002','122222')
# 接收返回的json数据
        jsonData=response.json()
        #输出
        logging.info("密码错误时输出数据：{}".format(jsonData))
#         断言
        assert_common(self,response,200,False,20001,"用户名或密码错误")





    def test04_username_have_special_char(self):
        # 调用封装的登录接口
        response = self.login_api.login('@#', '123456')
        # 接收返回的json数据
        jsonData = response.json()
        # 输出
        logging.info("特殊字符数据：{}".format(jsonData))
        #         断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")


    def test05_username_is_empty(self):
        # 调用封装的登录接口
        response = self.login_api.login('', '123456')
        # 接收返回的json数据
        jsonData = response.json()
        # 输出
        logging.info("账号为空：{}".format(jsonData))
        #         断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")


    def test06_password_is_empty(self):
        # 调用封装的登录接口
        response = self.login_api.login('13800000002', '')
        # 接收返回的json数据
        jsonData = response.json()
        # 输出
        logging.info("密码为空输出数据：{}".format(jsonData))
        #         断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")


    def test07_username_have_chinese(self):
        # 调用封装的登录接口
        response = self.login_api.login('1380想220002', '123456')
        # 接收返回的json数据
        jsonData = response.json()
        # 输出
        logging.info("账号有中文：{}".format(jsonData))
        #         断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")


    def test08_username_have_space(self):
        # 调用封装的登录接口
        response = self.login_api.login('1380000 002', '123456')
        # 接收返回的json数据
        jsonData = response.json()
        # 输出
        logging.info("用户名有空格：{}".format(jsonData))
        #         断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

























