import allure


class TestAllure:

    # def test_a(self):
    #     print("aa")
    #     assert 1

    # def test_b(self):
    #     print("bb")
    #     assert 1

    @allure.step(title="登录测试步骤")
    def test_login(self):
        allure.attach('登录', '输入用户名')
        print("输入用户名")
        allure.attach('登录', '输入密码')
        print("输入密码")
        allure.attach('登录', '点击登录')
        print("点击登录按钮")
        assert 1
