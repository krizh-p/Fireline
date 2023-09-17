from django import forms
from django.http import HttpResponse
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

from django.utils import timezone
import os

def new(request):
    if request.method == "POST":
        # Make sure you specify 'enctype="multipart/form-data"' in your HTML form for file uploads
        uploaded_file = request.FILES.get('image')
        print("Posting")
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        
        if uploaded_file:

            # Generate a unique filename based on a timestamp
            # timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
            # file_extension = os.path.splitext(uploaded_file.name)[-1]
            # unique_filename = f'uploads/{timestamp}{file_extension}'
            
            # # Save the uploaded file with the unique filename
            # with open(unique_filename, 'wb') as destination:
            #     for chunk in uploaded_file.chunks():
            #         destination.write(chunk)
            
            # Now, you can do further processing with the saved file if needed.
            
            # Return a response or redirect as needed
            return render(request, 'map/live.html', {
                "long" : longitude,
                "lat" : latitude
            })
        else:
            return HttpResponse('No file selected or invalid file format.')
    
    return render(request, 'live.html')