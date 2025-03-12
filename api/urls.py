from django.urls import path
from api import views

urlpatterns = [
    path("api/", views.getData),
    path("stats/", views.contact_stats),
]
