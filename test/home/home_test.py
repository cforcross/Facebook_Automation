import unittest
from pages.homePage.home_page import Home
from selenium import webdriver
import time
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class Home_Test:

    def valid_sign_up(self):

        baseUrl = 'https://www.facebook.com/'
        # binary = FirefoxBinary('C:/Users\phoex/.geckodriver')
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        h = Home(driver)
        h.enter_values("chowa", "cross", "imthebest", "ntsendifor@gmail.com")
        time.sleep(3)
        h.enter_second("ntsendifor@gmail.com")
        h.birth_day()
        h.gender(male="male")

        driver.quit()



    def invalid_sign_up(self):
        pass


ff = Home_Test()
ff.valid_sign_up()
