from base.customseleniumdrivers import SeleniumDriver
import time


class Home(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)

    # locators
    first_name = 'u_0_m'
    surname = 'u_0_o'
    email = 'u_0_r'
    email2 = 'reg_email_confirmation__'
    password = 'u_0_w'
    day = 'day'
    month = 'month'
    year = 'year'
    female_radio = 'u_0_6'
    male_radio = 'u_0_7'
    custom_radio = 'u_0_8'
    value = '17'
    EXPECTED_COLOR = "rgb(255, 0, 0)"
    exclamation = "_5dbc img sp_nK4QBEPgZVv sx_5b4a54"



    def enter_name(self, name):
        self.sendkeys(name, self.first_name, locatorType="id")

    def enter_surname(self, surname):
        self.sendkeys(surname, self.surname, locatorType="id")

    def enter_email(self, email):
        self.sendkeys(email, self.email, locatorType="id")

    def enter_email2(self, email2):
        self.sendkeys(email2, self.email, locatorType="name")

    def enter_passoword(self, data):
        self.sendkeys(data, self.password, locatorType="id")

    def select_day(self):
        self.selections(self.day, locatorType='id', index=18)

    def select_month(self):
        self.selections(self.day, locatorType='id', index=10)

    def select_year(self):
        self.selections(self.day, locatorType='id', value='2010')

    def female_gender(self):
        self.clickelement(self.female_radio, locatorType="id")

    def male_gender(self):
        self.clickelement(self.male_radio, locatorType="id")

    def custom_gender(self):
        self.clickelement(self.custom_radio, locatorType="id")

    #####               ########
    # GROUPED METHODS #
    #####               ########

    def enter_values(self, name, surname, password, email):
        self.enter_name(name)
        self.enter_surname(surname)
        self.enter_passoword(password)
        self.enter_email(email)


    def enter_second(self, email2):
        self.waitForElement(self.email2)
        self.enter_email(email2)

    def birth_day(self):
        self.select_day()
        self.select_month()
        self.select_year()

    def gender(self, male=" ", female=" ", custom=" "):
        male = male.lower()
        female = female.lower()
        custom = custom.lower()

        if female == "female":
            return self.female_gender()
        elif male == "male":
            return self.male_gender()
        elif custom == "custom":
            return self.custom_gender()
        else:
            print("You are neither male nor female nor custom")

    def invalid(self):
        result = self.elementpresencecheck(self.exclamation, locatorType='class')
        return result
