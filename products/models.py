from django.db.models import Model, CharField, DecimalField, TextField, DateTimeField, FloatField
from django.utils import timezone
# # Create your models here.
#
class Product(Model):
    CATEGORY = (
        ('Tapyba', 'Tapyba'),
        ('Grafika', 'Grafika'),
        )
    title = CharField(max_length=50, null=True)
    price = DecimalField(max_digits=10, decimal_places=2, null=True)
    category = CharField(max_length=50, null=True, choices=CATEGORY)
    description = TextField()

class Order(Model):
    STATUS = (
        ('Laukiama', 'Laukiama'),
        ('Išvežta pristatymui', 'Išvežta pristatymui'),
        ('Pristatyta', 'Pristatyta'),
    )

    # customer = ManyToManyField(Customer)
    # cart = ManyToManyField(Cart)
    created = DateTimeField(auto_now_add=True)
    status = CharField(max_length=200, null=True, choices=STATUS)

