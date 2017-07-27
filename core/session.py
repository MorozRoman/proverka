from model.account import Account



class SessionHelper:

    def  __init__(self, app):
        self.app = app

    def login(self, account):
        wd = self.app.wd
        self.app.open_home_page()
        # login
        wd.find_element_by_class_name("mos-header__controls-login-button-enter").click()
        wd.find_element_by_id("alias").click()
        wd.find_element_by_id("alias").clear()
        wd.find_element_by_id("alias").send_keys(account.username)
        # password
        wd.find_element_by_id("aliaspswd").click()
        wd.find_element_by_id("aliaspswd").clear()
        wd.find_element_by_id("aliaspswd").send_keys(account.password)
        wd.find_element_by_id('outerlogin_button').click()

    def logout(self):
        wd = self.app.wd
        # logout mos.ru
        # time.sleep(2)
        wd.find_element_by_class_name('mos-layout-icon-dropdown_up').click()
        wd.find_element_by_class_name("mos-layout-auth-out").click()


    # Проверка на нахождение в учетке нужного пользователя
    def ensure_login(self, account):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(account.username):
                return
            else:
                self.logout()
        self.login(Account(account.username, account.password))


    # Проверка на нахождение в учетке при попытке выйти
    def ensure_logout(self):
        wd = self.app.wd
        wd.find_element_by_class_name('mos-layout-icon-dropdown_up').click()
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_class_name("mos-layout-auth-out").click()) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return len(wd.find_element_by_xpath('//div[@class="mos-header__controls-button"]//span[.="каширин сергей александрович"]'))
        # return len(wd.find_element_by_xpath('//div[contains(@class, "mos-header__controls-button")]//span[@class, "mos-header__controls-button-label"]')).text == "каширин сергей александрович"