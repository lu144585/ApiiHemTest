import unittest,logging
from api.loggin_api import LoginApi
from utils import assert_common, read_login_data
from parameterized.parameterized import parameterized

class TestIHRMLoginPara(unittest.TestCase):
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

    @parameterized.expand(read_login_data)
    def test_login(self,mobile,password,http_code,success,code,message):
        # 调用封装登录接口
        response=self.login_api.login(mobile,password)
       #接收返回的json数据
        jsonData=response.json()
        # 调试出登录接口返回数据，日志输出只能作为{}占位符
        logging.info("登录接口返回数据:{}".format(jsonData))

        # 断言
        # self.assertEqual(200,response.status_code) #断言响应状态码
        # self.assertEqual(True,jsonData.get("success")) #断言success
        # self.assertEqual(10000,jsonData.get("code"))  #断言code
        # self.assertIn("操作成功",jsonData.get("message")) #断言message

        assert_common(self,response,http_code,success,code,message)