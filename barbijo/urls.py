from django.urls import path
from . import views

app_name = "barbijo"

urlpatterns = [
    path('', views.index, name="index"),
    path('tps/', views.tps, name="tps"),
]