from django.urls import path
from app import views


urlpatterns = [
    path('', views.ClienteList.as_view(), name='list'),
    path('create/', views.ClienteCreate.as_view(), name='create')
]