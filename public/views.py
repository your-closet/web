from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *


@login_required
def index(request):
    site_dict = {
        "message": "hello world!",
    }
    return render(request, "public/index.html", site_dict)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'public/signup.html', {'form': form})


class CreateClothingItem(CreateView):
    model = ClothingItem
    fields = ['brand','color','pattern','size','is_advertisable']


class ClothingItemUpdate(UpdateView):
    model = ClothingItem
    fields = ['name']
    template_name_suffix = '_update_form'


class ClothingItemDelete(DeleteView):
    model = ClothingItem
    success_url = reverse_lazy('')