# Basic functional test

# from selenium import webdriver

# browser = webdriver.Firefox() 
# browser.get('http://localhost:8000') 

# assert 'Django' in browser.title  
# browser.quit() 

# using unittest

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def test_home_page(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Lists', self.browser.title)

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')