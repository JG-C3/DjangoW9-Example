# [코드 추가] redirect 추가
from django.shortcuts import render, redirect
# [코드 추가] UserCreationForm, AuthenticationForm 추가
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# [코드 추가] login 함수를 auth_login 으로, logout 함수를 auth_logout 으로 추가
from django.contrib.auth import login as auth_login, logout as auth_logout

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')
    else:
        form = UserCreationForm()
    context = {
        'type': '회원가입',
        'form': form,
    }
    return render(request, 'account/form.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('page:index')
    else:
        form = AuthenticationForm()
    context = {
        'type': '로그인',
        'form': form,
    }
    return render(request, 'account/form.html', context)

def logout(request):
    auth_logout(request)
    return redirect('page:index')
