from django.shortcuts import render,redirect
from django.urls import reverse_lazy
#from .forms import EmailAuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
#from .forms import EmailLoginView
#from .forms import EmailValidationOnLoginForm
from django.contrib.auth.views import LoginView
from django.views.generic import FormView
from .forms import CustomUserLoginForm
from django.shortcuts import redirect
'''
def login_view(request):
    form = LoginForm()
    print("Form %s",form)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                e_mail=form.cleaned_data.get('e_mail')
            )
            return HttpResponseRedirect(reverse_lazy('post/post_list'))
        else:
            messages.error(request, 'Usuario no registrado!')
    return render(request, 'users/login.html') 

#def login_view(request):
    #if request.method == 'POST':
    #    form = AuthenticationForm(data=request.POST)
    #    if form.is_valid():
    #        #return redirect('post_list')
    #        return HttpResponseRedirect(reverse_lazy('post_list'))
    #else:
    #    form = AuthenticationForm()
    #return render(request, 'users/login.html', {'form':form})
    #return render(request, 'users/login.html')

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data['e_mail']
            user = authenticate(request, email=email)
            if user is not None:
                login(request, user)
                return redirect('post/post_list')
            else:
                form.add_error(None, 'Correo electrónico o contraseña incorrectos.')
    else:
        form = LoginForm(request)
    return render(request, 'users/login.html', {'form': form})


class EmailLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = EmailValidationOnLoginForm
'''

class CustomUserLoginView(FormView):
    template_name = 'login.html'
    form_class = CustomUserLoginForm

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)

        if user is not None:
            login(self.request, user)
            return redirect('home')
        else:
            form.add_error(None, 'El correo electrónico o la contraseña son incorrectos')
            return self.form_invalid(form)
