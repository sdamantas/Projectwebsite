from django.db.models import Model, CharField, ImageField, DateTimeField, TextField, ForeignKey, DO_NOTHING
from django.contrib.auth.models import User


class Article(Model):
    title = CharField(max_length=100)
    image = ImageField(null=True,upload_to="images")
    description = TextField()
    user = ForeignKey(User, on_delete=DO_NOTHING)
    created_on = DateTimeField(auto_now_add=True)
