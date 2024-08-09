from django.urls import path
from .views import *
urlpatterns = [
    path("register/", RegisterView.as_view(), name="RegisterView"),
    path("login/", LoginView.as_view(), name="LoginView")
]
