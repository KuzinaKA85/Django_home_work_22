from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from blogs.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = "blogs/article_list.html"
    context_object_name = "articles"


class ArticleCreateView(CreateView):
    model = Article
    template_name = "blogs/article_form.html"
    fields = ['title_article', 'content_article', 'image_article', 'is_active', 'views_count']
    success_url = reverse_lazy('blogs:article_list')


class ArticleDetailView(DetailView):
    model = Article
    template_name = "blogs/article_detail.html"
    context_object_name = "article"


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = "blogs/article_form.html"
    fields = ['title_article', 'content_article', 'image_article', 'is_active', 'views_count']
    success_url = reverse_lazy('blogs:article_list')


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "article_confirm_delete.html"
    success_url = reverse_lazy('blogs:article_list')
