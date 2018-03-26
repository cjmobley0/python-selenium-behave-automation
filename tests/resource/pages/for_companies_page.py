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

class ForCompaniesElements:
    top_nav_solutions = [By.XPATH, "//ul[@class='main-nav']//*[@data-analytics='SolutionsLink']"]
