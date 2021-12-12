from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest
from behave import *

class MainFunctions:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://opensource-demo.orangehrmlive.com/')

    def click_button(self, xpath):
        self.driver.find_element(By.XPATH, xpath).click()

    def enter_info(self, xpath, text):
        self.driver.find_element(By.XPATH, xpath).send_keys(text)

    def get_our_user_id(self, our_info):
        self.id_cont = self.driver.find_element(By.XPATH, our_info).get_attribute('href')
        self.value = self.id_cont[(self.id_cont.index('=') + 1)::]
        self.needed_id = "ohrmList_chkSelectRecord_"+str(self.value)

    def checkbox(self):
        self.driver.find_element(By.ID, self.needed_id).click()
        self.click_button('//*[@id="btnDelete"]')
        self.click_button('//*[@id="dialogDeleteBtn"]')

    def check_if_exist(self):
        try:
            self.driver.find_element(By.ID, self.needed_id)
            return 1
        except NoSuchElementException:
            pass
            return 2

    def test(self, point):
        if(point == 1):
            assert self.check_if_exist() == 1, "test failed"
        else:
            assert self.check_if_exist() == 2, "test failed"

class Testing(MainFunctions):

    def enter(self):
        #1 Enter info and log in
        self.enter_info('/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[2]/input', 'Admin')
        self.enter_info('/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[3]/input', 'admin123')
        self.click_button('/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[5]/input')
    def add_user(self):
        #opening the page we need
        self.click_button('/html/body/div[1]/div[2]/ul/li[1]/a')
        self.click_button('/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/a')
        self.click_button('/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[2]/a')
        #add a new user and info
        self.click_button('/html/body/div[1]/div[3]/div[1]/div/div[2]/form/div[1]/input[1]')
        self.enter_info('/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[1]/input[1]', 'User123')
        self.click_button('/html/body/div[1]/div[3]/div/div[2]/form/fieldset/p/input[1]')
        self.click_button('/html/body/div[1]/div[3]/div[3]/div[2]/form/p/input')
        self.enter_info('/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[1]/input', 'USD - United States Dollar')
        self.enter_info('/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[2]/input', '1000')
        self.enter_info('/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[3]/input', '2000')
        self.click_button('/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/p/input[1]')
    def delete_user(self):
        # check and deletion of user
        self.click_button('/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/a')
        self.click_button('/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[2]/a')
        self.get_our_user_id("//*[contains(text(), 'User123')]")
        if self.check_if_exist() == 1:
            print("Visible")
        else:
            print("Not visible")
        self.test(1)
        self.checkbox()
        if self.check_if_exist() == 1:
            print("Visible")
        else:
            print("Not visible")
        self.test(2)

test = Testing()
test.enter()
test.add_user()
test.delete_user()


