from django import forms
from django.contrib.auth.forms import AuthenticationForm

'''
class LoginForm(AuthenticationForm):
    e_mail = forms.EmailField(label="Email", max_length=50)

    class Meta:
        fields = ('email')
        

class EmailValidationOnLoginForm(AuthenticationForm):
    def clean(self):
        email = self.cleaned_data.get('username')
        if email and not users.objects.filter(email=email).exists():
            raise forms.ValidationError('Correo electrónico no válido')
        return super().clean()
'''