from django.shortcuts import render
from . import data

# Create your views here.
def index(request):
    fireList = data.map_data()
    context = {'fireList':fireList}
    return render(request, "map/index.html", context)