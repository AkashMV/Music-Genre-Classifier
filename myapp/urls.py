from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("blues/", views.blues, name="blues"),
    path("classical/", views.classical, name="classical"),
    path("country/", views.country, name="country"),
    path("disco/", views.disco, name="disco"),
    path("hiphop/", views.hiphop, name="hiphop"),
    path("jazz/", views.jazz, name="jazz"),
    path("metal/", views.metal, name="metal"),
    path("pop/", views.pop, name="pop"),
    path("reggae/", views.reggae, name="reggae"),
    path("rock/", views.rock, name="rock"),
]