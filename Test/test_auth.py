from Pages.login.auth import AuthForm


class TestAuth(object):

    def test_auth(self, browser):
        pp = AuthForm(browser)
        assert "Log out" == pp.auth()