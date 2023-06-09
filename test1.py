# instence methods(setup(),test(),teardown())

# import unittest
# class TestCaseDemo(unittest.TestCase):
#     def setUp(self):
#         print("Setup method executed successfully")
#     def test01(self):
#         print("Test01 method executed successfully")
#     def test02(self):
#         print("Test02 method executed successfully")
#     def tearDown(self):
#         print("Tear down method executed successfully")
# if __name__ == '__main__':
#     unittest.main()

# class methods(SetUpClass,TearDownClass() for this we use @classmethod decorators)

import unittest
class TestCaseDemo(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("Setup method executed successfully")
    def test_B01(self):
        print("Test_B01 method executed successfully")
    def test_A02(self):
        print("Test_A02 method executed successfully")
    @classmethod
    def tearDownClass(self):
        print("Tear down method executed successfully")
if __name__ == '__main__':
    unittest.main()
