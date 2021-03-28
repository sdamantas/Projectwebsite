from django.forms import ModelForm, ImageField
from blog.models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = "__all__"

