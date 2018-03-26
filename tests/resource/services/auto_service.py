#Page Objects Import
from tests.resource.pages.home_page import HomePageElements as HPE
from tests.resource.pages.signup_login_page import SignUpLoginElements as SLE
from tests.resource.pages.for_companies_page import ForCompaniesElements as FCE

from tests.resource.properties.main_properties import MainProperties as MP

class AutomationServices:
    def __init__(self):
        pass

    def getPageType(self, page_type):
        PageType = {
            'HomePage': HPE
        }
        return PageType[page_type]()

    #Associate expected by_elements for each URL page
    def getExpectedElmt(self, url):
        # Key: Page user is currently in
        # Value: Element that is expected to be there after navigating to said key page

        ee = {
            MP.hr_prod_url : HPE.hackerrank_logo,
            MP.hr_products_url : FCE.top_nav_solutions,
            MP.hr_login_url : SLE.login_tab,
            MP.hr_signup_url : SLE.sign_up_tab

        }
        return ee[url]