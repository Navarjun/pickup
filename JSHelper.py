from selenium import webdriver

class JSHelper:

    def __init__(self):
        ## Message: 'chromedriver' executable needs to be in PATH.
        ##
        try:
            self.browser = webdriver.Chrome("chromedriver 2")
        except e:
            print(e)

    def renderJS(self, url):
        self.browser.get(url)

    def close(self):
        self.browser.quit()
