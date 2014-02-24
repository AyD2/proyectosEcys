
from django.test import TestCase
from sistema_pe.models import Usuario
from hashlib import sha512
from sistema_pe import login
#Create your tests here.


class Unittest_Login(TestCase):

    def preparar(self):
        c = sha512('clave').hexdigest()
        c2 = sha512('clave2').hexdigest()
        Usuario.objects.create(nombre='usuario', clave=c)
        Usuario.objects.create(nombre='usuario2', clave=c2)

    def test_login_login(self):
        self.preparar()
        us = Usuario.objects.get(nombre='usuario')
        us2 = Usuario.objects.get(nombre='usuario2')
        self.assertEquals(login.login('usuario', 'clave'),True
                                    , "Si loguea satisfactoriamente")
        self.assertEquals(login.login('usuario2', 'clave'), False
                                     , "Si evita los loguins incorrectos")

    def test_login_db(self):
        self.preparar()
        usFalso = login.obtener_usuario('nombreFalso')
        usVerdadero = login.obtener_usuario('usuario')
        self.assertIsNone(usFalso)
        self.assertIsNotNone(usVerdadero)
                                                                                                                                            
