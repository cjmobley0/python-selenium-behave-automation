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

class SignInPageObjects:
    HACKERRANK_LOGO = [By.XPATH, "//img[@class='dark-logo-img']"]
