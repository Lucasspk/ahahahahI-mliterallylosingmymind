from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('filter/', views.filter_components, name='filter_components'),
    path('update_components/', views.update_components, name='update_components'),

]