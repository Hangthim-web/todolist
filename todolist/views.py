from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DeleteView, UpdateView, CreateView, DetailView

from todolist.models import Todolist


# Create your views here.


class HomePageView(TemplateView):
    model = Todolist
    template_name = "home.html"
    # context_object_name = "todolist_list"


class TodolistViewPage(LoginRequiredMixin, ListView):
    model = Todolist
    template_name = "todolist_list.html"

    def test_func(self):
        obj = self.get_object();
        return obj.user == self.request.user


class TodolistDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Todolist
    template_name = "todolist_delete.html"
    success_url = reverse_lazy("todolistView")

    def test_func(self):
        obj = self.get_object();
        return obj.user == self.request.user


class TodolistUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Todolist
    template_name = "todolist_update.html"
    fields = [
        "task",

        "end_date",
    ]

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class TodolistCreateView(LoginRequiredMixin, CreateView):
    model = Todolist
    template_name = "todolist_create.html"
    fields = [
        "task",
        "end_date",
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TodolistDetailView(LoginRequiredMixin, DetailView):
    model = Todolist
    template_name = "todolist_detail.html"


    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user
