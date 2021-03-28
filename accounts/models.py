from django.db.models import Model, CharField,  EmailField, DateTimeField


class Customer(Model):
    first_name = CharField(max_length=50, null=True)
    last_name = CharField(max_length=50, null=True)
    email = EmailField(max_length=50, null=True)
    gender = CharField(verbose_name='gender', max_length=15, choices=[('male', 'male'), ('female', 'female')],
                       null=True)
    phone = CharField(max_length=20, null=True)
    created = DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.first_name

