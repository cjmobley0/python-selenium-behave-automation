import logging, os, time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By

LOG = logging.getLogger(__name__)

class WebDriverApi:

    def __init__(self):
        pass

    def instance(self, browser):
        if 'firefox' in browser.lower():
            self.current_browser = 'Firefox'
            self.instance = webdriver.Firefox()
            self.instance.implicitly_wait(2)
        elif 'chrome' in browser.lower():
            self.current_browser = 'Chrome'
            chrome_capabilities = DesiredCapabilities.CHROME
            chrome_capabilities['logginPrefs'] = {'browser' : 'ALL'}
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--no-sandbox')
            self.instance = webdriver.Chrome( '/Users/Chris/chromedriver/chromedriver' , chrome_options=chrome_options, desired_capabilities=chrome_capabilities)
            self.instance.implicitly_wait(2)

        browser = self.instance


    def tear_down(self):
        try:
            self.instance.quit()
        except WebDriverException:
            LOG.info("Driver Failure: Unable to close driver")
        except (AttributeError, TypeError) as e:
            LOG.info("Browser not located. Try changing driver handler")

    def find_element_by(self, by_type, locator):
        by_type = by_type.lower()
        web_element = None

        try:
            if by_type == "id":
                web_element = self.instance.find_element(By.ID, locator)
            elif by_type == "xpath":
                web_element = self.instance.find_element(By.XPATH, locator)
            elif by_type == "link_text":
                web_element = self.instance.find_element(By.LINK_TEXT, locator)
            elif by_type == "partial_link_text":
                web_element = self.instance.find_element(By.PARTIAL_LINK_TEXT, locator)
            elif by_type == "name":
                web_element = self.instance.find_element(By.NAME, locator)
            elif by_type == "tag_name":
                web_element = self.instance.find_element(By.TAG_NAME, locator)
            elif by_type == "class_name":
                web_element = self.instance.find_element(By.CLASS_NAME, locator)
            elif by_type == "css_selector":
                web_element = self.instance.find_element(By.CSS_SELECTOR, locator)
            else:
                LOG.info("Unable to classify selector type.")
                LOG.info("Verify syntax and element identifier (ie. id, name, xpath, css_selector...) is correct")
                LOG.info("Element in question: " + str(web_element))
                raise Exception()

        except:
            raise Exception("Failed to identify element")

        return web_element


    def wait_for_element_by(self, by_type, locator, timeout=30):
        by_type = by_type.lower()
        web_element = None

        try:
            if by_type == "id":
                WebDriverWait(self.instance, timeout).until(lambda d : d.find_element(By.ID, locator))
            elif by_type == "xpath":
                WebDriverWait(self.instance, timeout).until(lambda d : d.find_element(By.XPATH, locator))
            elif by_type == "link_text":
                WebDriverWait(self.instance, timeout).until(lambda d : d.find_element(By.LINK_TEXT, locator))
            elif by_type == "partial_link_test":
                WebDriverWait(self.instance, timeout).until(lambda d : d.find_element(By.PARTIAL_LINK_TEXT, locator))
            elif by_type == "name":
                WebDriverWait(self.instance, timeout).until(lambda d : d.find_element(By.NAME, locator))
            elif by_type == "tag_name":
                WebDriverWait(self.instance, timeout).until(lambda d : d.find_element(By.TAG_NAME, locator))
            elif by_type == "class_name":
                WebDriverWait(self.instance, timeout).until(lambda d : d.find_element(By.CLASS_NAME, locator))
            elif by_type == "css_selector":
                WebDriverWait(self.instance, timeout).until(lambda d : d.find_element(By.CSS_SELECTOR, locator))
            elif by_type == "xpath":
                WebDriverWait(self.instance, timeout).until(lambda d : d.find_element(By.XPATH, locator))
            else:
                LOG.info("Unable to classify selector type.")
                LOG.info("Verify syntax and element identifier (ie. id, name, xpath, css_selector...) is correct")
                LOG.info("Element in question: " + str(web_element))
                raise Exception()

        except:
            raise Exception("Failed to identify element")


    def browser_launch(self, endpoint):

        if self.current_browser == 'Chrome':
            try:
                self.instance.set_window_size(1366, 768)
                self.instance.get(endpoint)
            except Exception, e:
                print (e)
        else:
            self.instance.maximize_window()
            self.instance.get(endpoint)



