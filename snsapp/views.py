from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import SnsModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return render(request, 'signup.html', {'welcome':'アカウントを登録しました！'})
        except IntegrityError:
            render(request, 'signup.html', {'error':'このユーザ名は既に登録されています'})
    return render(request, 'signup.html', {})

def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html', {'context': 'ユーザ名またはパスワードが間違っています'})
    return render(request, 'login.html', {})

@login_required
def listfunc(request):
    object_list = SnsModel.objects.all()
    return render(request, 'list.html', {'object_list': object_list})

def logoutfunc(request):
    logout(request)
    return redirect('login')

def detailfunc(request, pk):
    object = get_object_or_404(SnsModel, pk=pk)
    return render(request, 'detail.html', {'object':object})

def goodfunc(request, pk):
    object = SnsModel.objects.get(pk=pk)
    object.good = object.good + 1  
    object.save()
    return redirect('list')

def readfunc(request, pk):
    object = SnsModel.objects.get(pk=pk)
    username = request.user.get_username()
    if username in object.readtext:
        return redirect('list')
    else:
        object.read = object.read + 1
        object.readtext = object.readtext + ' ' + username
        object.save()
        return redirect('list')    

class SnsCreate(CreateView):
    template_name = 'create.html'
    model = SnsModel
    fields = ('title', 'content', 'author', 'snsimage')
    success_url = reverse_lazy('list')

    