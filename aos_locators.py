from faker import Faker

fake = Faker(locale='en-CA')
# -------------------LOCATOR SECTION-----------------------------------------------
app = 'Advantage online shopping'
aos_url = 'https://advantageonlineshopping.com/#/'
aos_home_page_title = '\u00A0Advantage Shopping'
registration_page ='https://advantageonlineshopping.com/#/register'

#--------------------DATA-------------------------------------------
username= 'TB'+ fake.first_name()[:10]
email=f'{username}@cctb.com'
password = 'Pass123'