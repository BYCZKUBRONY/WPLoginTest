import unittest
from selenium import webdriver
import time


class PythonWpLoginTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        time.sleep(5)
        self.browser.quit()

    def test_good_website(self):
        self.browser.get("https://profil.wp.pl")
        assert self.browser.current_url == "https://profil.wp.pl/login.html?idu=100&url=%2Fwizytowka.html%3F"

    def test_log_in_us(self,):
        self.log_in_us("wsb_bdd", "stxnext_bdd")

    def log_in_us(self, login, password):
        self.browser.get("https://profil.wp.pl")
        user_input = self.browser.find_element_by_id("login")
        user_input.clear()
        user_input.send_keys(login)
        password_input = self.browser.find_element_by_id("password")
        password_input.clear()
        password_input.send_keys(password)
        self.browser.find_element_by_id("btnSubmit").click()
        loged_user = self.browser.find_element_by_class_name("topuser__email.text-truncate")
        assert loged_user.text == "wsb_bdd@wp.pl"


if __name__ == "__main__":
    unittest.main()
