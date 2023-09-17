from django import forms
from django.shortcuts import render
from . import data, prediction

#Trained Data Predictions
predictedPoints = prediction.train(data.prediction_data())

class NewTaskForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content")
    image = forms.ImageField(label="Image", required=True)


# Create your views here.
def index(request):
    fireList = data.map_data()
    context = {'fireList':fireList}
    return render(request, "map/index.html", context)

def upload(request):
    return render(request, "map/upload.html", {
        "form" : NewTaskForm()
    })

def live(request):
    predictedPoints = {'fireList' : 'ADD FIRELIST HERE'}
    return render(request, "map/live.html", predictedPoints)