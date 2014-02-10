from django.test import LiveServerTestCase
from selenium import webdriver

# Create your tests here.

class LoginTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_login(self):
        assert 'foo' in 'bar'
        self.browser.get(self.live_server_url)

        body = self.browser.find_element_by_tag_name('body')
        assert "Django administration" in body.text
        
        self.fail('algo')


