from selene import be


class Application(object):

    def __init__(self, browser):
        self.browser = browser

    def open_with_extension(self):
        self.open_pw_extension_html()
        self.enter_pw_seed()
        self.enter_pw_name()
        self.enter_pw_passwords()

        self.open_acala_website()
        self.approve_connection()
        self.wait_until_acala_wallet_page_is_loaded()

    def open_pw_extension_html(self):
        self.browser.open("chrome-extension://mopnmbcafieddcagagdcbnhejhlodfdd/index.html")
        self.browser.element("button .children").should(be.visible).click()
        self.browser.element(".popupToggle").should(be.visible).click()

    def wait_until_acala_wallet_page_is_loaded(self):
        self.browser.switch_to_previous_tab()
        self.browser.element(".ant-modal").should(be.visible)
        self.browser.element(".aca-btn-style--normal").should(be.visible).click()

    def approve_connection(self):
        self.browser.driver.execute_script("window.open('');")
        self.browser.switch_to_next_tab().open("chrome-extension://mopnmbcafieddcagagdcbnhejhlodfdd/notification.html")
        self.browser.element(".children").should(be.visible).click()

    def open_acala_website(self):
        self.browser.open("https://apps.acala.network")
        self.browser.element(".sc-ezbkgU.gajIi").should(be.visible)
        self.browser.element("#mandala").with_(timeout=10000).should(be.visible)

    def enter_pw_passwords(self):
        polkawallet_password = "iut6&%G^&5H*&^(("
        self.browser.element("input[type='password']").should(be.visible).type(polkawallet_password)
        self.browser.element("input[type='password'][value='']").should(be.visible).type(polkawallet_password)
        self.browser.element("button + button").should(be.visible).click()

    def enter_pw_name(self):
        polkawallet_name = "test_polkawallet"
        self.browser.element("input[type='text']").should(be.visible).type(polkawallet_name)

    def enter_pw_seed(self):
        self.browser.element("[href='#/account/import-seed']").should(be.visible).click()
        polkawallet_seed = "squeeze ahead actress off material move fantasy fancy fatal find cram among"
        self.browser.element("textarea").should(be.visible).type(polkawallet_seed)
        self.browser.element("button .children").should(be.visible).click()
