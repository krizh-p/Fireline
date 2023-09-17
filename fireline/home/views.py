from django.shortcuts import render

from . import data, prediction

#Trained Data Predictions
predictedPoints = prediction.train(data.prediction_data)

# Create your views here.
def index(request):
    return render(request, "home/index.html")