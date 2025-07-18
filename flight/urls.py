from django.urls import path
from .import views

urlpatterns=[
    path ("" ,views.index , name="flight_index"),
    path ("<int:flight_id>" , views.get_flight, name = "flights"),
    path("<int:flight_id>/book", views.book , name="book")
]