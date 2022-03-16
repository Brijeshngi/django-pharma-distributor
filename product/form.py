from django import forms



from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User


'''
class studentregistration(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()

	'''

class registerform(UserCreationForm):
	
	class Meta:
		model = User
		fields = [ 'first_name', 'last_name', 'username', 'email']