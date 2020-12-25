from selenium import webdriver
from time import sleep
import config
import sys
import time
import json

username = config.username
password = config.password

print(' ')
print(' ')
print(' ')
print(' ')

print('an auto roller for aimgods by max')
print('hope ya win a mouse or sumn :)')

# Add the file path for your Chrome Driver or use PATH
driver = webdriver.Chrome('chromedriver.exe') 


driver.get("https://aimgods.finalmouse.com/goldenKey")

username_button = driver.find_element_by_xpath(
    "/html/body/div/div/div/div/div/form/input[1]"
)
username_button.send_keys(username)
password_button = driver.find_element_by_xpath(
    "/html/body/div/div/div/div/div/form/input[2]"
)
password_button.send_keys(password)

time.sleep(0.001)

login_button = driver.find_element_by_xpath(
    "/html/body/div/div/div/div/div/form/button"
)
login_button.click()

time.sleep(2)

driver.get("https://aimgods.finalmouse.com/goldenKey")

time.sleep(2)

while True:
    use_golden_key_button = driver.find_element_by_xpath(
        "/html/body/div/div/div/div/div/div[1]/div[1]/div[1]/div/button"
    )
    use_golden_key_button.click()

    # sleep for 30 seconds while the roll spins
    time.sleep(30)
    play_again = driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/div/div[1]/button'
    )
    play_again.click()

    time.sleep(2)
