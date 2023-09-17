from django.urls import path
from . import views

app_name = "map"

urlpatterns = [
    path("", views.index, name="index"),
    path("upload", views.upload, name="upload"),
    path("live", views.live, name="live")
]