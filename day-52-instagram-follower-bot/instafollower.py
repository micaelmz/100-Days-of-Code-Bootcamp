from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


class InstaFollower(webdriver.Chrome):

    def __init__(self):
        super().__init__(executable_path="C:/Micael/chromedriver.exe")
        self.endpoint = "https://www.instagram.com/"

    def login(self, account_user, account_pass):
        url = self.endpoint + "accounts/login/"
        self.get(url)
        sleep(2)
        self.find_element(By.NAME, "username").send_keys(account_user)
        self.find_element(By.NAME, "password").send_keys(account_pass + Keys.ENTER)

    def load_followers_page(self, target_account):
        url = self.endpoint + target_account + "/followers/"
        self.get(url)

    def find_followers(self):
        # sometimes the last enumerated div isn't 2 but 1
        followers = self.find_elements(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div')
        return followers

    def follow(self, follower):
        follower_button = follower.find_element(By.TAG_NAME, "button")
        if follower_button.text == "Seguir":
            follower_button.click()
            return True
        return False