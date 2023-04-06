from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home/', views.home, name='home'),
    path('about/',views.about, name='about'),
    path('theories/',views.theories,name='theories'),
    path('prisoner/', views.prisoner, name='prisoner')
]