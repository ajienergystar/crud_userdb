import logging
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets

from .models import CustomUser
from .serializers import UserSerializer
from .forms import CustomUserCreationForm

# Logger setup
logger = logging.getLogger('user_login')


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        logger.info(f"LOGIN : {user}")
        if user:
            login(request, user)
            return redirect('user_list')
        else:
            return render(request, 'login.html', {'error': 'Email atau password salah'})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'index.html', {'users': users})


def add_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        fullname = request.POST['fullname']
        password = request.POST['password']

        user = get_user_model()(
            username=username,
            email=email,
            fullname=fullname
        )
        user.set_password(password)
        user.save()

        return redirect('user_list')
    return render(request, 'add_user.html')


def edit_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.fullname = request.POST['fullname']
        user.save()
        return redirect('user_list')
    return render(request, 'edit_user.html', {'user': user})


def delete_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.delete()
    return redirect('user_list')
