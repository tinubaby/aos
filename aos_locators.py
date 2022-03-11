from faker import Faker

fake = Faker(locale='en-CA')
# -------------------LOCATOR SECTION-----------------------------------------------
app = 'Advantage online shopping'
AOS_url = 'http://advantageonlineshopping.com/#/'
AOS_home_page_title = '\u00A0Advantage Shopping'
registration_page ='http://advantageonlineshopping.com/#/register'

#--------------------DATA-------------------------------------------
username= fake.first_name()[:10]
email=f'{username}@cctb.com'
password = 'Pass123'