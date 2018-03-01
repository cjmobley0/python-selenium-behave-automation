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
    hackerrank_logo = [By.XPATH, "//img[@class='dark-logo-img']"]
    top_nav_developers = [By.XPATH, "//*[contains(@class, 'active') and contains(@class, 'pjR')]"]
    top_nav_for_companies = [By.XPATH, "//*[contains(@class,'sub-menu-2 homepage-dropdown')]"]
    top_nav_for_school = [By.XPATH, "//*[contains(@@@data-analytics,'ForSchoolsLink') and contains(@class, 'pjR')]"]