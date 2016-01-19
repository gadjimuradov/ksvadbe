import unittest 
from selenium import webdriver

class TestURLs(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()

	def tearDown(self):
		self.driver.close()

	def test_add_new_post(self):
		self.driver.get("http://localhost:5000/login")
		username_field = self.driver.find_element_by_name("username")
		username_field.send_keys("admin")
		password_field = self.driver.find_element_by_name("password")
		password_field.send_keys("adminadmin")
		login_button = self.driver.find_element_by_id("enter")
		login_button.click()

		self.driver.get("http://localhost:5000/blog/new")
		title_field = self.driver.find_element_by_name("title")
		title_field.send_keys("Test title")
       
        self.driver.switch_to.frame(
            self.driver.find_element_by_tag_name("iframe")
        )
        post_field = self.driver.find_element_by_class_name(
            "cke_editable"
        )
        post_field.send_keys("Test content")
        self.driver.switch_to.parent_frame()

        post_button = self.driver.find_element_by_class_name("btn-primary")
        post_button.click()

        # verify the post was created
        self.driver.get("http://localhost:5000/blog")
        self.assertIn("Test Title", self.driver.page_source)
        self.assertIn("Test content", self.driver.page_source)

if __name__ == "__main__":
	unittest.main()