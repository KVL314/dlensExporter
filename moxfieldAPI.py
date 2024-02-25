#!/usr/bin/python3
# Copyright [c] KVL314 [Derek Stiles](https://github.com/KVL314)

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common import exceptions

from webdriver_manager.chrome import ChromeDriverManager

import config
BASE_URL = 'https://www.moxfield.com'
LOGIN_URL = BASE_URL + '/account/signin?redirect=/'
DECK_URL= BASE_URL + '/decks/personal'


class moxAPI():
    def __init__(self):
        self.decks = {}

        options = Options()
        #options.add_argument('--headless')
        #options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def __call__(self):
        self.driver.close()

    def login(self):
        self.driver.get(LOGIN_URL)
        creds = config.get_moxfield_creds()
        print(self.driver.title)
        self.driver.find_element(By.ID, 'username').send_keys(creds['username'])
        self.driver.find_element(By.ID, 'password').send_keys(creds['password'])
        self.driver.find_element(By.CLASS_NAME, 'btn-primary').click()
        self.driver.implicitly_wait(0.5)
        sleep(1)

    def get_decks(self):
        self.driver.get(DECK_URL)
        print(self.driver.title)
        rows = self.driver.find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            print('in row')
            try:
                link = row.find_element(By.TAG_NAME, 'a')
                self.decks[link.text] = {
                    'href': link.get_dom_attribute('href')
                }
            except exceptions.NoSuchElementException:
                print("element not found")

        print(self.decks)

mox = moxAPI()
mox.login()
mox.get_decks()
print('waiting ...')
sleep(100)
