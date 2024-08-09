from django.urls import path
from .views import *
urlpatterns = [
    path("", ContactList.as_view(), name="ContactList"),
    path("<int:id>", ContactdetailView.as_view(), name="ContactdetailView")
]



