from django.shortcuts import render, redirect
from django.contrib.auth import(
    authenticate,
    login,
    logout,
    get_user_model,
)

from .forms import userLoginForm, userRegisterForm

#Giriş ve Kayıt işlemleri için kullanılan formlar ile Giriş, Kayıt ve Çıkış işlemlerinin view'ları
#Django'nun hazır formları kullanıldığı için formda kullanılan kelimeler İngilizce olarak bırakılmıştır
def login_view(request):
    loginForm = userLoginForm(request.POST or None)

    if loginForm.is_valid():
        username = loginForm.cleaned_data.get('username')
        password = loginForm.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if not request.user.is_staff:
            login(request, user)
            return redirect('/iha/new_iha')
    return render(request, 'form.html', {'form': loginForm, 'title': 'Giriş Yap'})

def register_view(request):
    registerForm = userRegisterForm(request.POST or None)

    if registerForm.is_valid():
        user = registerForm.save(commit=False)
        password = registerForm.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        return redirect('/login/')
    return render(request, 'form.html', {'form': registerForm, 'title': 'Kayıt Ol'})

def logout_view(request):
    logout(request)
    return render(request, 'home.html', {})