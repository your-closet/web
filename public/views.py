from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.files.storage import FileSystemStorage
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
            p = Profile(
                user = user
            )
            p.save()
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
            site_dict = {"message": "Form is invalid"}
            return render(request, "public/index.html", site_dict)
    else:
        tops = ClothingItem.objects.filter(
            profile=request.user.profile, clothing_type="top")
        try:
            top_images = [
                Image.objects.filter(clothing_item=top)[0] for top in tops
            ]
        except IndexError:
            top_images = []
        bottoms = ClothingItem.objects.filter(
            profile=request.user.profile, clothing_type="bottom")
        try:
            bottom_images = [
                Image.objects.filter(clothing_item=bottom)[0]
                for bottom in bottoms
            ]
        except IndexError:
            bottom_images = []
        site_dict = {
            "tops": tops,
            "bottoms": bottoms,
            "bottom_images": bottom_images,
            "top_images": top_images,
        }
        return render(request, "public/index.html", site_dict)


@login_required
def add_clothing(request):
    if request.method == "POST":

        # get the potential forms form the web page
        clothing_type_form = ClothingTypeForm(request.POST)
        clothing_form = ClothingForm(request.POST)
        image_form = ImageForm(request.POST)

        # if we have a full add_clothign post
        if clothing_form.is_valid():
            c = ClothingItem(
                profile=request.user.profile,
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
                image_file = request.FILES['image']
                i = Image(clothing_item=c, image=image_file)
                i.save()
                return redirect("/")
            else:
                return JsonResponse({"message": "Image Not Valid."},
                                    status=400)

        # if we're loading from index
        elif clothing_type_form.is_valid():
            clothing_type = clothing_type_form.cleaned_data.get(
                "clothing_type")
            site_dict = {
                "clothing_type": clothing_type,
                "clothing_form": ClothingForm(),
                "image_form": ImageForm()
            }
            return render(request, "public/add_clothing.html", site_dict)

        # if the forms are invalid
        else:
            return JsonResponse({"message": "Something went wrong."},
                                status=400)
    else:
        site_dict = {
            "clothing_form": ClothingForm(),
            "image_form": ImageForm()
        }
        return render(request, "public/add_clothing.html", site_dict)


def test(request):
    return render(request, "public/test.html")


def get_image(clothing_item):
    try:
        image = Image.objects.filter(clothing_item=clothing_item).first()
        return str(image.image)
    except:
        return None


def get_clothing_item_and_images(profile, clothing_type):
    q = ClothingItem.objects.filter(
        profile=profile, clothing_type=clothing_type)

    return [
        dict(
            brand=item.brand,
            color=item.color,
            pattern=item.pattern,
            price=item.price,
            size=item.size,
            clothing_type=item.clothing_type,
            is_advertisable=item.is_advertisable,
            image=get_image(item)) for item in q
    ]


@login_required
def get_clothing(request):
    tops, bottoms, shoes = [
        get_clothing_item_and_images(request.user.profile, "top"),
        get_clothing_item_and_images(request.user.profile, "bottom"),
        get_clothing_item_and_images(request.user.profile, "shoe"),
    ]

    return JsonResponse({
        "tops": tops,
        "bottoms": bottoms,
        "shoes": shoes
    }, status=200)