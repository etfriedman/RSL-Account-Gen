from selenium import webdriver
from random import getrandbits
import time
import csv
from random_username.generate import generate_username

option = webdriver.ChromeOptions()
option.add_argument("-incognito")

browser = webdriver.Chrome(executable_path="chromedriver.exe", options=option)
browser.get("your url here") #REPLACE URL HERE
#insert CPaths as strings (make sure to leave the quotes) i.e: username_input = '//*[@id="root"]/div/div/div/div/div/div/div[4]/div[1]/div/form/div[3]/label/input'
username_input = ''
password_input = ''
email_input = ''
form_submit = ''
accept_button = ''

def make_account():
    generated_username = generate_username(1)
    email_ext = "@gmail.com"
    username = generated_username[0] # 4 extra nums
    password = getrandbits(30) # 6 numbers (min is 6)
    email = generated_username[0] + email_ext

    browser.find_element_by_xpath(username_input).send_keys(username)
    browser.find_element_by_xpath(password_input).send_keys(password)
    browser.find_element_by_xpath(email_input).send_keys(email)
    browser.find_element_by_xpath(form_submit).click()
    time.sleep(0.5)
    browser.find_element_by_xpath(accept_button).click()

    #write account details to file
    with open("accounts.csv", "a+", newline='') as csvfile:
        csvwriter = csv.writer(csvfile) 
        fields = [username, password, email]
        csvwriter.writerow(fields)

    print("Account Created: UN: ", username ,"PW:", password ,"EMAIL:" , email)
    
while True:
    make_account()
    time.sleep(0.5)
    browser.refresh()