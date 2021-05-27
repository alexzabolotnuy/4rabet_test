from selenium.webdriver.common.by import By

class Login(object):
    LOGIN = "//div[@class='v-text-field__slot']/descendant::input[@type='text']"
    PASS = "//div[@class='v-text-field__slot']/descendant::input[@type='password']"
    BUTTON_SIGNIN = "//div[@class='header__btn']/descendant::span[text()='Sign in']"
    BUTTON_LOGIN = "//div[@class='v-card__actions']/descendant::span[text()='Sign in']"
    BALANCE = "balance__sum desktop"