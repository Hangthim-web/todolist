from django.urls import path

from todolist.views import HomePageView, TodolistViewPage, TodolistUpdateView, TodolistDeleteView, TodolistCreateView, \
    TodolistDetailView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("view_list/", TodolistViewPage.as_view(), name="todolistView"),
    path("delete/<int:pk>", TodolistDeleteView.as_view(), name="deleteView"),
    path("edit/<int:pk>", TodolistUpdateView.as_view(), name="updateView"),
    path("create/", TodolistCreateView.as_view(), name="create"),
    path("detail/<int:pk>",TodolistDetailView.as_view(),name="detailView"),
]
