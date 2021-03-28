from django.db.models import Model, CharField, DecimalField, TextField, DateTimeField, ManyToManyField
from accounts.models import Customer
# # Create your models here.
#


class Tag(Model):
	name = CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Product(Model):
    CATEGORY = (
        ('Tapyba', 'Tapyba'),
        ('Grafika', 'Grafika'),
        )
    title = CharField(max_length=50, null=True)
    price = DecimalField(max_digits=10, decimal_places=2, null=True)
    category = CharField(max_length=50, null=True, choices=CATEGORY)
    description = TextField()
    tags = ManyToManyField(Tag)

    def __str__(self):
        return self.title

class Order(Model):
    STATUS = (
        ('Laukiama', 'Laukiama'),
        ('Išvežta pristatymui', 'Išvežta pristatymui'),
        ('Pristatyta', 'Pristatyta'),
    )

    customer = ManyToManyField(Customer, null=True, on_delete= SET_NULL)
    cart = ManyToManyField(Product, null=True, on_delete= SET_NULL)
    created = DateTimeField(auto_now_add=True)
    status = CharField(max_length=200, null=True, choices=STATUS)

