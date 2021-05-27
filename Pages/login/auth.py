from Locators.Login import Login


link = "https://4ra.4rabet.com/?bt-path=/live"

class AuthForm(object):

    def __init__(self, browser):
        self.browser = browser


    def frt (self):
        self.browser.get(link)
        self.browser.find_element_by_xpath(Login.BUTTON_SIGNIN).click()
        self.browser.find_element_by_xpath(Login.LOGIN).send_keys("cooper+20@deversin.com")
        self.browser.find_element_by_xpath(Login.PASS).send_keys("asdasdasd")
        self.browser.find_element_by_xpath(Login.BUTTON_LOGIN).click()

    def auth(self):
        self.frt()
        self.browser.implicitly_wait(30)
        Button = self.browser.find_element_by_class_name(Login.BALANCE).text
        return Button
