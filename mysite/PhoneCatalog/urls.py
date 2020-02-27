from django.urls import path

from . import views

app_name = 'PhoneCatalog'
urlpatterns = [
    path('', views.index, name='index')
]