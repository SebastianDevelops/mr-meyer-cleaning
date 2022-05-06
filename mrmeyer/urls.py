from django.urls import path
from .views import index, detergents, car_care, floor_care, disinfect
urlpatterns = [
    path("", index, name="home"),
    path("detergents/", detergents, name="detergents"),
    path("car-care/", car_care, name="car-care"),
    path("floor-care/", floor_care, name="floor-care"),
    path("sanatizers-and-disinfectants/", disinfect, name="disinfectants"),
]
