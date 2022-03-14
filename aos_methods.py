import sys
import aos_locators as locators

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # <---add this import for drop down list
from selenium.webdriver.common.keys import Keys

# s = Service(executable_path='C:\\Users\\aamykutty\\PycharmProjects\\pythonProject\\chromedriver.exe')
# driver = webdriver.Chrome(service=s)


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

def links():
    #1. Check that SPEAKERS, TABLETS, HEADPHONES, LAPTOPS, MICE texts are displayed.
    assert driver.find_element(By.ID,'speakersTxt').is_displayed(),'Error: Speaker not displayed'
    sleep(1)
    assert driver.find_element(By.ID, 'tabletsTxt').is_displayed(), 'Error: Tablet not displayed'
    sleep(1)
    assert driver.find_element(By.ID, 'laptopsTxt').is_displayed(), 'Error: Laptop not displayed'
    sleep(1)
    assert driver.find_element(By.ID, 'miceTxt').is_displayed(), 'Error: Mice not displayed'
    sleep(1)
    assert driver.find_element(By.ID, 'headphonesTxt').is_displayed(), 'Error: Headphones not displayed'
    sleep(1)
    assert driver.find_element(By.ID,'speakersLink').is_enabled(), 'Error: Shop now for Speaker not working'
    sleep(1)
    assert driver.find_element(By.ID,'tabletsLink').is_enabled(), 'Error: Shop now for Tablet not working'
    sleep(1)
    assert driver.find_element(By.ID,'laptopsLink').is_enabled(), 'Error: Shop now for Laptop not working'
    sleep(1)
    assert driver.find_element(By.ID,'miceLink').is_enabled(), 'Error: Shop now for Mice not working'
    sleep(1)
    assert driver.find_element(By.ID,'headphonesLink').is_enabled(), 'Error: Shop now for Headphones not working'
    sleep(1)
    assert driver.find_element(By.XPATH,'//article/h3[contains(.,"SPECIAL OFFER")]').is_displayed(),'ERROR: SPECIAL OFFER not displayed'
    sleep(1)

    assert driver.find_element(By.ID,'see_offer_btn').is_enabled(),'Error: OFFER Button not enabled'
    sleep(1)
    assert driver.find_element(By.XPATH,'.//li/a[contains(.,"OUR PRODUCTS")]').is_enabled(),'ERROR: OUR PRODUCT id not clickable'
    sleep(1)
    assert driver.find_element(By.XPATH,'.//li/a[contains(.,"SPECIAL OFFER")]').is_enabled(),'ERROR: SPECIAL OFFER is not clickable'
    sleep(1)
    assert driver.find_element(By.XPATH,'.//li/a[contains(.,"POPULAR ITEMS")]').is_enabled(),'ERROR: POPULAR ITEMS not clickable'
    sleep(1)
    assert driver.find_element(By.XPATH,'.//li/a[contains(.,"CONTACT US")]').is_enabled(),'ERROR: CONATCT US is not clickable'
    sleep(1)
    assert driver.find_element(By.XPATH,'.//div/a/span[contains(.,"dvantage")]').is_displayed(),'ERROR: LOGO not displayed'
    sleep(1)
    print("HOME PAGE -LINKS SUCCESSFULLY VALIDATED ")

def contactUs():

    Select(driver.find_element(By.NAME,'categoryListboxContactUs')).select_by_value('object:59')
    sleep(1)
    Select(driver.find_element(By.NAME,'productListboxContactUs')).select_by_visible_text('HP Chromebook 14 G1(ENERGY STAR)')
    sleep(1)
    driver.find_element(By.NAME,'emailContactUs').send_keys('abcd@gmail.com')
    sleep(1)
    driver.find_element(By.NAME,'subjectTextareaContactUs').send_keys('This is subject area text')
    sleep(1)
    driver.find_element(By.ID,'send_btnundefined').click()
    sleep(1)
    assert driver.find_element(By.XPATH,'.//p[contains(.,"Thank you for contacting Advantage support.")]').is_displayed(),'ERROR: THANK YOU message not displayed'
    sleep(1)
    assert driver.find_element(By.LINK_TEXT,'CONTINUE SHOPPING').is_enabled(),'ERROR: CONTINUE SHOPPING Button not enabled'
    sleep(1)
    assert driver.find_element(By.NAME,'follow_facebook').is_enabled(),'ERROR: FACEBOOK is not clickable'
    sleep(1)
    assert driver.find_element(By.NAME,'follow_twitter').is_enabled(),'ERROR: Twitter is not clickable'
    sleep(1)
    assert driver.find_element(By.NAME,'follow_linkedin').is_enabled(),'ERROR: LinkedIN is not clickable'
    sleep(1)
    print("HOME PAGE -CONTACT US SUCCESSFULLY VALIDATED ")
    print('HOME PAGE IS WORKING ')

def myOrders():
    sleep(1)
    driver.find_element(By.ID, 'menuUser').click()
    sleep(1)
    driver.find_element(By.XPATH, '//a/div/label[contains(.,"My orders")]').click()
    sleep(1)
    assert driver.find_element(By.XPATH,'//div/label[contains(.,"No order")]').is_displayed(),'Error: NO order not dispalyed'
    print('No orders displayed')
    sleep(1)
    driver.find_element(By.ID, 'menuUser').click()
    sleep(1)
    driver.find_element(By.XPATH, '//a/div/label[contains(.,"My account")]').click()
    sleep(1)
    driver.find_element(By.XPATH,'.//button[contains(@class,"deleteMainBtnContainer")]').click()
    sleep(1)
    driver.find_element(By.XPATH,'.//div[@class="deletePopupBtn deleteRed"]').click()
    sleep(3)
    driver.find_element(By.ID, 'menuUser').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@name="username"]').send_keys(locators.username)
    print(f' Username {locators.username} entered')
    sleep(1)
    driver.find_element(By.XPATH, '//*[@name="password"]').send_keys(locators.password)
    print(f' Password {locators.password} entered')
    sleep(1)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(1)
    assert driver.find_element(By.ID,'signInResultMessage').is_displayed(),'Error: Error message not dispalying'
    print("Error message Displayed")

#
# setUp()
# links()
# contactUs()
# create_account()
# logout()
# login()
# logout()
#login()
#myOrders()
# tearDown()