import logging, os, time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By

LOG = logging.getLogger(__name__)

BY_TYPES = [By.ID,
            By.XPATH,
            By.LINK_TEXT,
            By.PARTIAL_LINK_TEXT,
            By.NAME,
            By.TAG_NAME,
            By.CLASS_NAME,
            By.CSS_SELECTOR
            ]

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

    def tear_down(self):
        try:
            self.instance.quit()
        except WebDriverException:
            LOG.info("Driver Failure: Unable to close driver")
        except (AttributeError, TypeError) as e:
            LOG.info("Browser not located. Try changing driver handler")

    def find_element_by(self, by_locator):
        web_element = None

        try:
            if by_locator[0] in BY_TYPES:
                web_element = self.instance.find_element(*by_locator)
            else:
                LOG.info(" Invalid BY.[TYPE]...")
                raise Exception(LOG)
        except:
            return None

        if web_element == None:
            LOG.info(" Unable to classify selector type.")
            LOG.info(" Verify syntax and element identifier (ie. id, name, xpath, css_selector...) is correct")
            raise Exception(LOG)

        return web_element


    def wait_for_element_by(self, by_locator, timeout=30):
        web_element = None

        try:
            if by_locator[0] in BY_TYPES:
                WebDriverWait(self.instance, timeout).until(lambda d : d.find_element(*by_locator))
                return True
            else:
                LOG.info("Invalid BY.[TYPE]...")
                raise Exception(LOG)
        except:
            LOG.info(" Failed to identify element...")
            raise Exception(LOG)


    def browser_launch(self, endpoint):

        browser_type = self.instance.name

        if browser_type == 'chrome':
            try:
                self.instance.set_window_size(1366, 768)
                self.instance.get(endpoint)
            except Exception, e:
                print (e)
        else:
            self.instance.maximize_window()
            self.instance.get(endpoint)



