from tests.resource.pages.home_page import HomePageElements

class AutomationServices:
    def __init__(self):
        pass

    def getPageType(self, page_type):
        PageType = {
            'HomePage': HomePageElements
        }
        return PageType[page_type]()