from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import get_user_model, authenticate, logout, login

def criar_cliente(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_created = get_user_model().objects.create(
            email=email,
            # password=password
        )
        user_created.set_password(password)
        user_created.save()
        print(f'Email: {email} - Senha: {password}')

    return render(request, 'criar_cliente.html')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    return redirect(reverse('produtos:listar_produtos'))