from django.test import LiveServerTestCase
from selenium import webdriver


class Selenium_test2(LiveServerTestCase):

    def preparar(self):
        self.browser = webdriver.Firefox()
        self.browser.implicity_wait(3)
 
    def bajar(self):
        self.browser.quit()


    def pueden_entrar_a_admin_site(self):
        self.browser.get(self.live_server_url + '/admin/')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django admin', body.text)
        self.fail('fin de prueba')
