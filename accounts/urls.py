from django.urls import path

from accounts.views import SignupPageView
from todolist.views import HomePageView

urlpatterns = [
    path("home/", HomePageView.as_view(), name="accounts_home"),
    path("signup/",SignupPageView.as_view(),name = "signup"),
]