from django import forms
from .models import SubmitModel
from django.forms import widgets, FileInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MainForm(forms.ModelForm):


	class Meta:
		model = SubmitModel
		fields = '__all__'

		widgets = {
			'pic': FileInput(attrs={'image': 'image'})

		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		for i in self.fields:

			self.fields[i].widget.attrs['class'] = 'form-control m-3'
			self.fields[i].widget.attrs['style'] = 'height:37px; width: 300px;'
		self.fields['author'].required = False
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=False)


	class Meta:
		model = User

		fields = ("username", "email", "password1", "password2")
		help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }



	def save(self, commit=True):

		user = super(NewUserForm, self).save(commit=False)
		if commit:
			user.save()
		return user			
