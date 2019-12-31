import os
from dotenv import load_dotenv
from selenium import webdriver
from bs4 import BeautifulSoup
import requests


from selenium.webdriver.chrome.options import Options
import re

#chrome_options = Options()
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--window-size=1920,1080");
#chrome_options.add_argument("--start-maximized");
#chrome_options.add_argument("--headless");





# load env
load_dotenv()


# Authentication
driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

# locate email field
username = driver.find_element_by_id('username')

# fill with email stored in env
username.send_keys(os.getenv('EMAIL'))

# locate password field
password = driver.find_element_by_id('password')

# fill with password stored in env
password.send_keys(os.getenv('PASSWORD'))

# locate submit button
log_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

# trigger click event
log_in_button.click()

#go to any profile
driver.get('https://www.linkedin.com/in/nicolasfrolin/')



html = driver.page_source

soup = BeautifulSoup(html, 'lxml')

#print(soup.prettify())


emails = soup.find_all(text=re.compile('^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$'))
soup.find_all('a', {'href': re.compile('crummy\.com/')})

print(emails)

[print(email.get_text()) for email in emails]

driver.quit()


# driver.implicitly_wait(6) # seconds

