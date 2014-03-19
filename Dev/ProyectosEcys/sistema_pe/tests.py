
from django.test import TestCase
from sistema_pe.models import Usuario
from hashlib import sha512
from sistema_pe import login

#Create your tests here.


class Unittest_Login(TestCase):

    def preparar(self):
        c = sha512('clave').hexdigest()
        c2 = sha512('clave2').hexdigest()
        Usuario.objects.create(carnet='200819222', clave=c)
        Usuario.objects.create(carnet='200815489', clave=c2)

    def test_login_login(self):
        self.preparar()
        us = Usuario.objects.get(carnet='200819222')
        us2 = Usuario.objects.get(carnet='200815489')
        self.assertEquals(login.login('200819222', 'clave'),True
                                    , "Si loguea satisfactoriamente")
        self.assertEquals(login.login('200815489', 'clave'), False
                                     , "Si evita los loguins incorrectos")

    def test_login_db(self):
        self.preparar()
        usFalso = login.obtener_usuario('nombreFalso')
        usVerdadero = login.obtener_usuario('200819222')
        self.assertIsNone(usFalso)
        self.assertIsNotNone(usVerdadero)  



from django.test import LiveServerTestCase
from selenium import webdriver


class Selenium_test(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicity_wait(3)

    def tearDown(self):
        self.browser.quit()


    def pueden_entrar_a_admin_site(self):
        self.browser.get(self.live_server_url + '/admin/')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django admin', body.text)
        self.fail('fin de prueba')
