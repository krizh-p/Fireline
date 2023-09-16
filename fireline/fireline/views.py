from django.shortcuts import render

def index(request):
    # refers to index.html in frontend/build/index.html
    return render(request, "index.html")