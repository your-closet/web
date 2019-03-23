from django.shortcuts import render

def index(request):
    site_dict = {
        "message":"hello world!",
    }
    return render(request, "public/index.html", site_dict)