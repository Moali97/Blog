from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'first_name', 'last_name', 'body', 'genre']
    login_url = 'login'


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body', 'genre']
    login_url = 'login'


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

