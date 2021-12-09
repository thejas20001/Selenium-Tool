from selenium import webdriver
import unittest
from selenium.webdriver.edge.service import Service
import HtmlTestRunner
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class GoogleSearchEngineTest(unittest.TestCase):
    browser = None

    @classmethod
    def setUpClass(cls):
        s = Service('D:/Chrome Driver/chromedriver')
        cls.browser = webdriver.Chrome(service=s)


    def setUp(self):
        self.browser.get("https://www.google.com/")
        self.browser.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls) :
        cls.browser.quit()


    def testCase1_searchPuneethRaj(self):
        self.browser.find_element_by_name('q').send_keys('Puneeth Rajkumar')
        self.browser.find_element_by_name('btnK').click()


    def testCase2_searchMITT(self):
        self.browser.find_element_by_name('q').send_keys('MIT Thandavapura')
        self.browser.find_element_by_name('btnK').click()

    def testCase2_searchShivrajKumar(self):
        self.browser.find_element_by_name('q').send_keys('shivrajkumar')
        self.browser.find_element_by_name('btnK').click()

    def testCase2_searchTalkadu(self):
        self.browser.find_element_by_name('q').send_keys('talakadu')
        self.browser.find_element_by_name('btnK').click()


if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports/'))


