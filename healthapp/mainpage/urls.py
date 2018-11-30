from django.urls import path
from . views import User, User_detail


urlpatterns = [
    path('', User.as_view()),
    path('<int:pk>/', User_detail.as_view())
]