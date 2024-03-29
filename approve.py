import time
from selenium import webdriver

driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://tom-staging.lyft.net/users/1529241897037654594/applicant');

time.sleep(5) # Let the user actually see something!

username = driver.find_elements_by_css_selector("#okta-signin-username")[0]
username.send_keys("") // put your email address here
password = driver.find_elements_by_css_selector("#okta-signin-password")[0]
password.send_keys("") // put your okta password here
password.submit()

driver.quit()