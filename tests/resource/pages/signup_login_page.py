from selenium.webdriver.common.by import By

'''
List of valid By types:
ID 
XPATH 
LINK_TEXT 
PARTIAL_LINK_TEXT 
NAME 
TAG_NAME 
CLASS_NAME 
CSS_SELECTOR 

'''


class SignUpLoginElements:
    sign_up_tab = [By.XPATH, "//*[contains(@class, 'active')]//*[@href='/signup']"]
    login_tab = [By.XPATH, "//*[contains(@class, 'active')]//*[@href='/login']"]

