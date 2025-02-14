from selenium import webdriver
import unittest
from django.test import LiveServerTestCase


""" Basic functional test using selenium """
# browser = webdriver.Firefox() 
# browser.get('http://localhost:8000') 

# assert 'Django' in browser.title  
# browser.quit() 


"""Using unittest module and segregating the test into a class by refactoring the code"""

# class NewVisitorTest(unittest.TestCase):
#     def setUp(self):
#         self.browser = webdriver.Firefox()
    
#     def test_home_page(self):
#         self.browser.get('http://localhost:8000')
#         self.assertIn('Lists', self.browser.title)

#     def tearDown(self):
#         self.browser.quit()

# if __name__ == '__main__':
#     unittest.main(warnings='ignore')



""" Now we will use the LiveServerTestCase to run the functional tests"""
class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        self.browser.get(self.live_server_url)
        self.assertIn('Home', self.browser.title)



