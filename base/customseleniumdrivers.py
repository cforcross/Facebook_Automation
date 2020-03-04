from selenium.webdriver.common.by import By
import utilities.customlogger as cl
from selenium.webdriver.support.select import Select
import logging
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class SeleniumDriver:
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getbytype(self, locatorType):
        locatorType = locatorType.lower()

        if locatorType == "xpath":
            return By.XPATH
        elif locatorType == "id":
            return By.ID
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "text":
            return By.LINK_TEXT
        elif locatorType == "name":
            return By.NAME
        else:
            self.log.error(f"Locator type {locatorType} not found")

    def getelement(self, locator, locatorType="xpath"):
        element = None
        try:
            byType = self.getbytype(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info(f"Element Found with locator {locator}and  locatorType{locatorType}")
        except:
            self.log.error(f"Element not Found with locator {locator}and  locatorType{locatorType}")
        return element

    def clickelement(self, locator, locatorType):
        try:
            element = self.getelement(locator, locatorType='xpath')
            element.click()
            self.log.info(f"Element Found with locator {locator}and  locatorType{locatorType}")
        except:
            self.log.error(f"Element not Found with locator {locator}and  locatorType{locatorType}")

    def sendkeys(self, data, locator, locatorType='xpath'):
        try:
            element = self.getelement(locator, locatorType)
            element.send_keys(data)
            self.log.info(f"Data send with locator {locator}and  locatorType{locatorType}")
        except:
            self.log.error(f"Could not send data with locator {locator}and  locatorType{locatorType}")

    def selections(self, locator, locatorType, index=" ", value="", text=" "):
        try:
            element = self.getelement(locator, locatorType)
            sel = Select(element)
            if sel.select_by_index(index):
                self.log.info(f"found selectiion with index {index} locator: {locator} and locatortype: {locatorType}")
            elif sel.select_by_value(value):
                self.log.info(f"found selectiion with value {value}  locator: {locator} and locatortype: {locatorType}")
            elif sel.select_by_visible_text(text):
                self.log.info(f"found selectiion with text {text} locator: {locator} and locatortype: {locatorType}")
            else:
                self.log.error("selector not found")
        except:
            self.log.error("exception error raised")
            print_stack()

    def getelements(self, locator, locatorType):
        element = None
        try:
            bytype = self.getbytype(locatorType)
            element = self.driver.find_elements(locator, bytype)
            self.log.info(f"Elements found with {locator} and locatorType {locatorType}")
        except:
            self.log.error(f"Elements not found with {locator} and locatorType {locatorType}")
        return element

    def elementpresencecheck(self, locator, locatorType="id"):
        try:
            element = self.getelements(locator, locatorType)
            if element is not None:
                self.log.info(f"Element found with {locator} and locatorType{locatorType}")
                return True

            else:
                self.log.error(f"Element not found with {locator} and locatorType {locatorType}")
                return False
        except:
            self.log.error(f"Element not found with {locator} and locatorType {locatorType}")

    def waitForElement(self, locator, locatorType="id",
                       timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getbytype(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,
                                                             "stopFilter_stops-0")))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element
