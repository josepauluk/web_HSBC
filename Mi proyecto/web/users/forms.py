from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import PrependedText

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

class CustomUserLoginForm(AuthenticationForm):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'autofocus': True, 'class': 'form-control'}),
        label='Correo electrónico'
    )
    helper = FormHelper()
    helper.form_method = 'post'
    helper.add_input(Submit('submit', 'Iniciar sesión'))
