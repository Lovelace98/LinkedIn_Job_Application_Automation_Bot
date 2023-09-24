from selenium.common.exceptions import NoSuchElementException
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
service = Service()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager(driver_version="116.0.5845.141").install(), options=options))

"These are the variables required to log in at Linkedin"
ACCOUNT_EMAIL = "This is where I would enter my email"
ACCOUNT_PASSWORD = "This is where I would enter my password"
PHONE = "This is where I would enter my phone number"

#This is the link to the search results of your preferred job
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3656983339&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true")

time.sleep(2)

#This gets the sign in button and clicks on it
sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

#This waits for the page to load and then it fills in the username and password and then our bot presses enter
time.sleep(5)
email_field = driver.find_element(By.ID, "username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(5)

all_listings = driver.find_elements(By.CSS_SELECTOR ,".job-card-container--clickable")

#This block of code loops through the entire job listings with Easy Apply enabled. Our bot enters the phone number and then clicks on submit. Then it moves to the next one. 
for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR ,".jobs-s-apply button")
        apply_button.click()

        time.sleep(5)
        phone = driver.find_element(By.CLASS_NAME ,"fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)
        
        submit_button = driver.find_element(By.CSS_SELECTOR ,"footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            
            time.sleep(2)
            discard_button = driver.find_elements(By.CLASS_NAME,"artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME ,"artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()

