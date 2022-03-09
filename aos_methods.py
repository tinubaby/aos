import sys
import aos_locators as locators

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # <---add this import for drop down list
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# s = Service(executable_path='C:\\Users\\aamykutty\\PycharmProjects\\pythonProject\\chromedriver.exe')
# driver = webdriver.Chrome(service=s)
#-----------------GItHUB------
options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

def setUp():
    #print start day and time
    print(f'Start Date and Time{datetime.datetime.now()}')

    # browser full screen
    driver.maximize_window()

    # Give browser 30 sec to respond
    driver.implicitly_wait(5)

    #get to the URL: https://advantageonlineshopping.com/#/ (Links to an external site.)
    # (add it to aos_locators.py and import as a variable);
    # Navigate to aos app website
    driver.get(f'{locators.AOS_url}')

    #check/compare the driver.current_url with expected and driver.title with expected.
    # This should be in one conditional statement. if everything as expected - print user-friendly message;

    if driver.current_url == locators.AOS_url and driver.title == locators.AOS_home_page_title:
        print('Current page url and Title succussfully validated')
    else:
        #- if URL and title are not as expected, print user-friendly messages about incorrect destination.
        # close the browser and quit from session.

        print('You are at incorrect destination')
        tearDown()

def tearDown():
    #check if driver is working and not none;

    if driver is not None:

        #print test end day and time;

        print('---------------------------------------')
        print(f'Test End Day and Time:{datetime.datetime.now()} ')
        sleep(2)
        #- close the browser and quit from session
        driver.close()
        driver.quit()

def create_account():

    sleep(1)
    driver.find_element(By.ID,'menuUser').click()
    print(f'Click User Icon')
    sleep(3)
    driver.find_element(By.LINK_TEXT,'CREATE NEW ACCOUNT').click()
    print(f'Click create new account')
    sleep(1)
    driver.find_element(By.XPATH,'//*[@name="usernameRegisterPage"]').send_keys(locators.username)
    print(f' Username {locators.username} entered')
    sleep(1)
    driver.find_element(By.XPATH,'//*[@name="emailRegisterPage"]').send_keys(locators.email)
    print(f'Email {locators.email} entered')
    sleep(1)
    driver.find_element(By.XPATH, '//*[@name="passwordRegisterPage"]').send_keys(locators.password)
    print(f' Password {locators.password} entered')
    sleep(1)
    driver.find_element(By.XPATH, '//*[@name="confirm_passwordRegisterPage"]').send_keys(locators.password)
    print(f' Confirm Password {locators.password} entered')
    sleep(1)
    driver.find_element(By.XPATH, './/*[@name="i_agree"]').click()
    print(f': I-Agree Check box clicked')
    sleep(1)
    driver.find_element(By.ID,'register_btnundefined').click()
    print(f' New user {locators.username} successfully registered.')
    print(f'TASK: CREATE NEW ACCOUNT: COMPLETED')
    sleep(1)
    if(driver.find_element(By.XPATH,f'.//a[@id="menuUserLink"]/span[contains(.,{locators.username})]').is_displayed() == True ):

        # Validate New Account created (new username is displayed in the top menu)

        assert driver.find_element(By.XPATH,f'//a[@id="menuUserLink"]/span[contains(.,{locators.username})]').is_displayed(), 'ERROR: USERNAME NOT DISPALYED AT MENU '
        print(f' USERNAME: {locators.username} DISPALYED AT MENU')
        print(f'TASK: Validate New Account is created: COMPLETED')
#-------------------------------LOG IN----------------------------------------------
def login():
    sleep(1)
    driver.find_element(By.ID, 'menuUser').click()
    print(f'Click User Icon')
    sleep(3)
    driver.find_element(By.XPATH, '//*[@name="username"]').send_keys(locators.username)
    print(f' Username {locators.username} entered')
    sleep(1)
    driver.find_element(By.XPATH, '//*[@name="password"]').send_keys(locators.password)
    print(f' Password {locators.password} entered')
    driver.find_element(By.ID,'sign_in_btnundefined').click()
    print('TASK: LOGIN : COMPLETED')
    sleep(2)
    assert driver.find_element(By.XPATH,f'//a[@id="menuUserLink"]/span[contains(.,{locators.username})]').is_displayed(), 'ERROR: USERNAME NOT DISPALYED AT MENU '
    print(f' USERNAME: {locators.username} DISPALYED AT MENU')
    print(f'TAKS : VALIDATE NEW USER CAN LOGIN : COMPLETED')

#---------------------------------LOG OUT-------------------------------------------------
def logout():
    sleep(1)
    driver.find_element(By.ID,'menuUserLink').click()
    sleep(1)
    driver.find_element(By.XPATH,'//a/div/label[contains(.,"Sign out")]').click()
    sleep(1)
    print(f'TASK: LOGOUT : COMPLETED')

# setUp()
# create_account()
# logout()
# login()
# logout()
# tearDown()