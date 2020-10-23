from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_CHOICES =(
    ('S','Shirt'),
    ('SW','Sport wear'),
    ('OW','Outwear')
)
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    slug = models.SlugField()
    description = models.TextField()
    item_pic = models.ImageField(upload_to='uploads',null=True)

    def __str__(self):
        return self.title



class OrderItem(models.Model):
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.item.title

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    order_date = models.DateField(auto_now_add=True, null=True)


    def __str__(self):
        return self.ordered
    
