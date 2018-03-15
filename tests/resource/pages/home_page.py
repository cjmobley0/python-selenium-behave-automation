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

class HomePageElements:
    hackerrank_logo = [By.XPATH, "//img[@class='dark-logo-img']"]
    top_nav_developers = [By.XPATH, "//*[contains(@class, 'active') and contains(@class, 'pjR')]"]
    top_nav_for_companies = [By.XPATH, "//*[contains(@class,'sub-menu-2 homepage-dropdown')]"]
    top_nav_for_school = [By.XPATH, "//*[contains(@data-analytics,'ForSchoolsLink') and contains(@class, 'pjR')]"]
    top_nav_login_button = [By.XPATH, "//a[@data-analytics='LoginBtn']"]
    top_nav_signup_button = [By.XPATH, "//a[@data-analytics='SignupBtn']"]