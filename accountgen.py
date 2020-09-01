from selenium import webdriver
from random import getrandbits
import time
import csv

option = webdriver.ChromeOptions()
option.add_argument("-incognito")

browser = webdriver.Chrome(executable_path="chromedriver.exe", options=option)
browser.get("your url here")
username_input = ''
password_input = ''
email_input = ''
form_submit = ''
accept_button = ''

def make_account():
    username = 'username-prefix{}'.format(getrandbits(12)) # 4 extra nums
    password = getrandbits(30) # 6 numbers (min is 6)
    email = 'email-prefix{}@gmail.com'.format(getrandbits(12))

    #fills out form and clicks buttons!
    browser.find_element_by_xpath(username_input).send_keys(username)
    browser.find_element_by_xpath(password_input).send_keys(password)
    browser.find_element_by_xpath(email_input).send_keys(email)
    browser.find_element_by_xpath(form_submit).click()
    #wait for popup window
    time.sleep(0.7)
    browser.find_element_by_xpath(accept_button).click()

    #write account details to csv file
    with open("accounts.csv", "a+", newline='') as csvfile:
        csvwriter = csv.writer(csvfile) 
        fields = [username, password, email]
        csvwriter.writerow(fields)

    print("Account Created: UN: ", username ,"PW:", password ,"EMAIL:" , email)
    
while True:
    make_account()
    #could maybe speed this up
    time.sleep(1)
    #refresh to clear and make a new account
    browser.refresh()
