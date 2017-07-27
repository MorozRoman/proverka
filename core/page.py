

class PagesHelper:

    def  __init__(self, app):
        self.app = app

    def add_drivers_license(self, drivers_license):
        wd = self.app.wd
        self.go_to_profile()
        wd.find_element_by_class_name('tab-profile').click()
        wd.find_elements_by_xpath('//h2[contains(@class, "add-doc-btn")]/a').click()
        self.fill_drivers_license_form(drivers_license)


    def go_to_profile(self):
        wd = self.app.wd
        # Оптимизация переходов между страницами
        if not (wd.current_url.endswith('/my/#profile')):
            wd.find_element_by_class_name('mos-layout-icon-dropdown_up').click()
            wd.find_element_by_link_text("Профиль").click()

    def fill_drivers_license_form(self, drivers_license):
        wd = self.app.wd
        self.input_text("input-text", drivers_license.serial_number)
        self.input_text("hasDatepicker", drivers_license.date_issue)
        wd.find_element_by_class_name('btn-save').click()
        wd.find_element_by_class_name('btn-subscr-save').click()

    def input_text(self, field_text, text):
        wd = self.app.wd
        # Конструкция if then else:
        if text is not None:
            wd.find_element_by_class_name(field_text).click()
            wd.find_element_by_class_name(field_text).clear()
            wd.find_element_by_class_name(field_text).send_keys(text)