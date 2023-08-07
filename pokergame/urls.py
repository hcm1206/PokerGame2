from django.urls import path

from .views import pokergame_base_views

app_name = 'pokergame'

urlpatterns = [
    # base_views.py
    path('',
         pokergame_base_views.index, name='index'),

]