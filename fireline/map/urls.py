from django.urls import path
from . import views

app_name = "map"

urlpatterns = [
    path("", views.index, name="index"),
    path("live", views.live, name="live"),
    path("test", views.new, name="new")
]