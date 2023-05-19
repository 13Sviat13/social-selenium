import time

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import configuration


class SocialNetworkScraper:

    BASE_URL = f"http://{configuration.SOCIAL_NETWORK_HOST}:{configuration.SOCIAL_NETWORK_PORT}"
    REGISTER_URL = f"{BASE_URL}/auth/register"
    LOGIN_URL = f"{BASE_URL}/auth/login"
    BLOG_URL = F"{BASE_URL}/user/blog"
    def __init__(self):
        self.driver = None

    def create_driver(self):
        try:
            self.driver = webdriver.Chrome(executable_path=configuration.CHROME_DRIVER_PATH)
            return self.driver
        except Exception as e:
            print(e.args)

    def social_network_registration(self):
        driver = self.create_driver()
        driver.get(self.REGISTER_URL)

        username_elem = driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='username']")
        username_elem.send_keys(configuration.SOCIAL_NETWORK_USERNAME)
        time.sleep(1)

        email_elem = driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='email']")
        email_elem.send_keys(configuration.SOCIAL_NETWORK_EMAIL)
        time.sleep(1)

        password_elem = driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='password']")
        password_elem.send_keys(configuration.SOCIAL_NETWORK_PASSWORD)
        time.sleep(1)

        password_confirm_elem = driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='confirm_password']")
        password_confirm_elem.send_keys(configuration.SOCIAL_NETWORK_PASSWORD)
        password_confirm_elem.send_keys(keys.Keys.ENTER)
        time.sleep(1)

        logout_elem = self.driver.find_element(By.XPATH, "//li[@class='nav-item me-2']/a[@class='nav-link']")
        logout_elem.click()

        return driver

    def social_network_login(self, login_required=True):
        if login_required:


            self.driver.get(self.LOGIN_URL)

            login_elem = self.driver.find_element(By.ID, 'username')
            login_elem.send_keys(configuration.SOCIAL_NETWORK_USERNAME)
            time.sleep(1)

            password_elem = self.driver.find_element(By.ID, 'password')
            password_elem.send_keys(configuration.SOCIAL_NETWORK_PASSWORD)
            time.sleep(1)
            password_elem.send_keys(keys.Keys.ENTER)



    def social_network_post(self, title, content, login_registered=True):
        if login_registered:
            self.driver = self.social_network_registration()

        self.social_network_login()


        self.driver.get(self.BLOG_URL)
        time.sleep(1)

        title_elem = self.driver.find_element(By.ID, 'title')
        title_elem.send_keys(title)
        time.sleep(1)

        content_elem = self.driver.find_element(By.ID, 'content')
        content_elem.send_keys(content)
        time.sleep(1)

        create_post_elem = self.driver.find_element(By.XPATH, "//form/button[@type='submit']")
        create_post_elem.click()
        time.sleep(1)

        like_post_elem = self.driver.find_element(By.XPATH, "//div[@class='btn-group']/a[@href]")
        like_post_elem.click()
        time.sleep(1)

        delete_post_elem = self.driver.find_element(By.XPATH, "//div[@class='btn-group']/a[@class='btn btn-sm btn-outline-danger']")
        delete_post_elem.click()
        time.sleep(1)

        logout_elem = self.driver.find_element(By.XPATH, "//li[@class='nav-item me-2']/a[@class='nav-link']")
        logout_elem.click()

        self.social_network_login()
