from django import forms
from django.shortcuts import render

class NewTaskForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content")
    image = forms.ImageField(label="Image")

# Create your views here.
def index(request):
    return render(request, "fireform/index.html")

def new(request):
    if request.method == "POST":
        # Take in the data the user submitted and save it as form
        print("Image Submitted")
    return