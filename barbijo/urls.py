from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('ale', views.ale, name="ale"),
    path('propuesta',views.propuesta,name="propuesta"),
    path('about',views.about,name="about"),
    path('galeria',views.galeria,name="galeria"),

]
