from django.urls import path
from . import views

# Config urls
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.base, name="about")
]
