from django.urls import path

from blogs.apps import BlogsConfig

from blogs.views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
)

app_name = BlogsConfig.name

urlpatterns = [
    path("article/", ArticleListView.as_view(), name="article_list"),
    path("article/new/", ArticleCreateView.as_view(), name="article_form"),
    path("article/<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path(
        "article/update/<int:pk>/", ArticleUpdateView.as_view(), name="article_update"
    ),
    path(
        "article/delete/<int:pk>/", ArticleDeleteView.as_view(), name="article_confirm_delete",),
]
