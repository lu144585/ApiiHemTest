import time
import unittest
import app
from script.login import Login
from script.test_emp import TestIHRMEmp

from script.test_login import TestIHRMLogin
from tools.HTMLTestRunnerCN import HTMLTestReportCN

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(Login))
suite.addTest(unittest.makeSuite(TestIHRMEmp))

# suite.addTest(unittest.makeSuite(TestIHRMLogin))
# 使用HTMLTestRunner执行测试套件生成测试报告
report_path = app.BASE_DIR + "/report/ihrm{}.html".format(time.strftime('%Y%m%d %H%M%S'))
with open(report_path,mode='wb')as f:
    runner= HTMLTestReportCN(f,verbosity=1,title="IHRM人力资源接口测试",description="v1.0.0")
    runner.run(suite)















