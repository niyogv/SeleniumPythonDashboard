import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# login cred
username='user@16ju'
password='Test@123'

# edit profile
fname='niyog'
lname='v'
mail='niyog@google.com'
number='9999999999'

# update profile
firstname='nihal'
lastname='v'
e='niyog@yahoo.co.in'
phone='8888888888'

# bio
bio='tester'

# update bio
updatebio='qa'

class Test_dashboard:

    @pytest.fixture()
    def test_invoke(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://qadashboard.iome.ai')
        self.driver.maximize_window()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//button').click()
        self.driver.find_element(By.XPATH, '//input[@placeholder="Username"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(6)
        check=self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/section/section/div/div[1]')
        assert check.text=='Hello!', 'Login failed'

    def test_kyc(self,test_invoke):
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/section/section/section/main/div/div[1]/div[2]/button[1]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div[1]/label/span[1]/input').click()
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/button').click()
        time.sleep(6)
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/section/section/section/main/div/div[1]/div/article').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/section/section/section/main/div/div[1]/div[2]/button[1]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/label/span[1]/input').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/button').click()
        time.sleep(6)

    def test_edit_profile(self,test_invoke):
        self.driver.find_element(By.XPATH, '//button[2]').click()
        time.sleep(2)
        check1=self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/button/span')
        assert check1.text=='Save information', 'Edit profile page is broken'
        self.driver.find_element(By.XPATH, '//input[@placeholder="What is your first name?"]').send_keys(fname)
        self.driver.find_element(By.XPATH, '//input[@placeholder="What is your last name?"]').send_keys(lname)
        self.driver.find_element(By.XPATH, '//input[@placeholder="unique@rmail.com"]').send_keys(mail)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div').click()
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[2]/ul/li[1]').click()
        self.driver.find_element(By.XPATH, '//input[@placeholder="Enter phone number"]').send_keys(number)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/button').click()
        time.sleep(4)

    def test_update_profile(self,test_invoke):
        self.driver.find_element(By.XPATH, '//button[2]').click()
        time.sleep(2)
        check2=self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/button/span')
        assert check2.text=='Save information', 'Update page is broken'
        first=self.driver.find_element(By.XPATH, '//input[@placeholder="What is your first name?"]')
        for f in range(5):
            first.send_keys(Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, '//input[@placeholder="What is your first name?"]').send_keys(firstname)
        self.driver.find_element(By.XPATH, '//input[@placeholder="What is your last name?"]').send_keys(Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, '//input[@placeholder="What is your last name?"]').send_keys(lastname)
        e_mail=self.driver.find_element(By.XPATH, '//input[@placeholder="unique@rmail.com"]')
        for m in range(16):
            e_mail.send_keys(Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, '//input[@placeholder="unique@rmail.com"]').send_keys(e)
        phone_number=self.driver.find_element(By.XPATH, '//input[@placeholder="Enter phone number"]')
        for w in range(10):
            phone_number.send_keys(Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, '//input[@placeholder="Enter phone number"]').send_keys(phone)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/button').click()
        time.sleep(4)

    @pytest.mark.flaky(rerun=2)
    def test_bio(self,test_invoke):
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//textarea').send_keys(bio)
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/section/section/section/main/div/div[2]/div[2]/div/div/div/div/div[3]/div[2]/button').click()
        time.sleep(2)

    @pytest.mark.flaky(rerun=2)
    def test_update_bio(self,test_invoke):
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//img[@alt="edit icon"]').click()
        b=self.driver.find_element(By.XPATH, '//textarea')
        for y in range(6):
            b.send_keys(Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, '//textarea').send_keys(updatebio)
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/section/section/section/main/div/div[2]/div[2]/div/div/div/div/div[3]/div[2]/button').click()
        time.sleep(2)

    @pytest.mark.flaky(rerun=2)
    def test_social(self,test_invoke):
        time.sleep(2)
        twit=self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/section/section/section/main/div/div[2]/div[1]/div[2]/div/div/div[2]/div[1]/div[2]/a')
        time.sleep(3)
        twit.click()
        time.sleep(4)
        self.driver.back()
        time.sleep(2)
        discord=self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/section/section/section/main/div/div[2]/div[1]/div[2]/div/div/div[2]/div[2]/div[2]/a')
        discord.click()
        time.sleep(4)


