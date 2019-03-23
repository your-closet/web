from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *


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


@login_required
def index(request):
    if request.method == "POST":
        form = ClothingTypeForm(request.POST)
        if form.is_valid():
            site_dict = {
                "clothing_type": form.cleaned_data.get("clothing_type")
            }
            return redirect('add_clothing')
        else:
            site_dict = {
                "message": "Form is invalid"
            }
            return render(request, "public/index.html", site_dict)
    else:
        site_dict = {
            "message": "hello world!",
        }
        return render(request, "public/index.html", site_dict)


@login_required
def add_clothing(request):
    if request.method == "POST":
        clothing_type_form = ClothingTypeForm(request.POST)
        clothing_form = ClothingForm(request.POST)
        image_form = ImageForm(request.POST)
        if clothing_form.is_valid():
            c = ClothingItem(
                user_id=request.user.profile,
                brand=clothing_form.cleaned_data.get("brand"),
                color=clothing_form.cleaned_data.get("color"),
                pattern=clothing_form.cleaned_data.get("pattern"),
                size=clothing_form.cleaned_data.get("size"),
                clothing_type=clothing_form.cleaned_data.get("clothing_type"),
                is_advertisable=clothing_form.cleaned_data.get(
                    "is_advertisable"),
                price=0,
            )
            c.save()
            if image_form.is_valid():
                i = Image(
                    clothing_item_id=c,
                    image_data=image_form.cleaned_data.get("image_data")
                )
                i.save()
                return JsonResponse({"redirect": "/"}, status=200)
            else:
                return JsonResponse({"message": "Image Not Valid."}, status=400)
        elif clothing_type_form.is_valid():
            clothing_type = clothing_type_form.cleaned_data.get("clothing_type")
            site_dict = {
                "clothing_type": clothing_type,
                "clothing_form": ClothingForm(),
                "image_form": ImageForm()
            }
            return render(request, "public/add_clothing.html", site_dict)
        else:
            return JsonResponse({"message": "Clothing Form Not Valid"}, status=400)
    else:
        site_dict = {
            "clothing_form": ClothingForm(),
            "image_form": ImageForm()
        }
        return render(request, "public/add_clothing.html", site_dict)
