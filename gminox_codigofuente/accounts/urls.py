from django.urls import path
from . import views

urlpatterns = [
    path(r'signup/', views.SignUp.as_view(), name='signup'),
]
