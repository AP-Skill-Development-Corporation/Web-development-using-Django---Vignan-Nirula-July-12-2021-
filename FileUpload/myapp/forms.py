from django import forms
from .models import Images

class ImagesForm(forms.ModelForm):
	class Meta:
		model = Images
		fields = '__all__'
		# fields = ['name','image']



		widgets = {
		'name' : forms.TextInput(attrs = {'class':'form-control'}),
		'image' : forms.FileInput(attrs = {'class':'form-control'})
		}