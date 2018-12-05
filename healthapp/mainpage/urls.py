from django.urls import path
from . import views


urlpatterns = [
    path('', views.UserDetail, name='User'),
    path('<Users/int:pk>', views.UserDetail)
]