# -*- coding: utf-8" -*
import unittest
from selenium import webdriver
import time


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_footer_link_size(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        time.sleep(3)
        login_btn = driver.find_element_by_class_name("login")
        login_btn.click()
        time.sleep(3)
        footer_box_link = driver.find_element_by_xpath("//ul[@class='bullet']")
        footer_link = footer_box_link.find_elements_by_tag_name("li")
        self.assertEqual(4, len(footer_link))


if __name__ == "__main__":
    unittest.main(verbosity=2)