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
        # Gertrude opens her web browser, and goes to the admin page
        self.browser.get(self.live_server_url + '/')
        # She sees the familiar 'Django administration' heading
        body = self.browser.find_element_by_tag_name('body')
        #print body.text
        #self.assertEquals('AboutTerminosAyuda', str(body.text))
        self.assertEquals('AboutTerminosAyuda' == body.text, True, 'algo')
        # TODO: use the admin site to create a Poll
        #self.fail('finish this test')
