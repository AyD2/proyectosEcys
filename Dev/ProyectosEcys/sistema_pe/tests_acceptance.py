from django.test import TestCase
  
# Create your tests here.
from django.test import LiveServerTestCase
from selenium import webdriver
 
class PollsTest(LiveServerTestCase):
 
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)
 
    def tearDown(self):
        self.browser.quit() 
  
    def test_puede_entrar_a_index(self):
        self.browser.get(self.live_server_url + '/')
        body = self.browser.find_element_by_tag_name('body')
        self.assertEquals('AboutTerminosAyuda' == body.text, True, 'algo')
        #self.fail('finish this test')
