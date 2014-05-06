from django.forms import ModelForm
from django import forms
#from sistema_pe import Clase, Usuario, Proyecto
from django.conf import settings
#from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import filesizeformat

class UploaderForm(forms.Form):
	'''
	Uploader form
	'''

	enunciado = forms.FileField()
	def clean_upload(self):
		enunciado = self.cleaned_data['upload']
                return enunciado

