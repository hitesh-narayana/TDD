from selenium import webdriver
import unittest
from django.contrib.staticfiles.testing import LiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
# class NewVisitorTest(LiveServerTestCase):
#     def setUp(self):
#         self.browser = webdriver.Firefox()
    
#     def tearDown(self):
#         self.browser.quit()

#     def test_home_page(self):
#         self.browser.get(self.live_server_url)
#         self.assertIn('Home', self.browser.title)



""" Now we will add more tests to the class"""
class NewVisitorTest(LiveServerTestCase):
    
    def setUp(self):
        """Set up Selenium WebDriver"""
        self.browser = webdriver.Chrome()  

    def tearDown(self):
        """Quit browser after test"""
        self.browser.quit()

    def test_can_save_a_POST_request(self):
        """Test if a new list item can be saved via POST request"""
        
        # Open the form page
        self.browser.get(self.live_server_url + reverse('view_list'))

        # Wait for the input field to be visible
        inputbox = WebDriverWait(self.browser, 10).until(
            # Added 'id_name' to the locator to find the input field
            # Changed the locator to find the input field by ID
            # added widget to the input field in the form to give it an ID
            EC.presence_of_element_located((By.ID, "id_name"))
        )
        # Enter new item and submit
        inputbox.send_keys("A new list item")
        # find XPath of the submit button
        submit_button = self.browser.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()

        # Wait for redirect and check if the item was added
        WebDriverWait(self.browser, 10).until(
            EC.url_matches(self.live_server_url + "/")  # Ensure it redirects correctly
        )







