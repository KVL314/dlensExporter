#!/usr/bin/python3
# Copyright [c] KVL314 [Derek Stiles](https://github.com/KVL314)



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdrivermanager.chrome import ChromeDriverManager
#from webdrivermanager.

service = webdriver.ChromeService(executable_path='/usr/bin/chromium-browser')


options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')


driver = webdriver.Chrome(service=service, options=options)
#driver = webdriver.Chrome(service=Service(ChromeDriverManager()), options=options)

#driver = webdriver.Firefox(service=Service(ChromeDriverManager().install()), options=options)





'''

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title

driver.implicitly_wait(0.5)

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

text_box.send_keys("Selenium")
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
text = message.text

driver.quit()













from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdrivermanager.chrome import ChromeDriverManager
from webdrivermanager.

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

#driver = webdriver.Firefox(service=Service(ChromeDriverManager().install()), options=options)
driver = webdriver.Firefox(service=Service(ChromeDriverManager()), options=options)

driver.get("https://python.org")
print(driver.title)
driver.close()
'''
'''
aLOGIN='https://www.moxfield.com/account/signin?redirect=/'
driver = webdriver.Firefox()
driver.get(LOGIN)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get(LOGIN)
'''
