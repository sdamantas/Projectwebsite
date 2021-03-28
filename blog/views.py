from django.shortcuts import reverse
from django.urls import reverse_lazy
from blog.models import Article
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from blog.forms import ArticleForm


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "ArticleCreateView.html"
    success_url = reverse_lazy("blog:CreateArticle")

#    def get_success_url(self):
#        article_id = Article.objects.last()
#        return str(article_id.id)


class ArticleListView(ListView):
    model = Article
    template_name = "ArticleListView.html"


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy("blog:ListArticle")
    template_name = "ArticleUpdateView.html"


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy("blog:CreateArticle")
    template_name = "ArticleDeleteView.html"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "ArticleDetailView.html"

