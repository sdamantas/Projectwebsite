from django.urls import path
from blog.views import ArticleCreateView, ArticleListView, ArticleDeleteView, ArticleDetailView, ArticleUpdateView


app_name = "blog"

urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name='CreateArticle'),
    path('articles/<pk>/', ArticleDetailView.as_view(), name='ArticleDetail'),
    path('<pk>/delete/', ArticleDeleteView.as_view(), name='ArticleDelete'),
    path('<pk>/update/', ArticleUpdateView.as_view(), name='ArticleUpdate'),
    path('articles/', ArticleListView.as_view(), name='ListArticle'),
]
