import unittest
from name_function import get_formatted_name

class NameTestCacse(unittest.TestCase):
    """测试name_functiom"""
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name=get_formatted_name("elon","musk")
        self.assertEqual(formatted_name,"Elon Musk")#类的断言函数，检测预期是否与真实一致

unittest.main()

