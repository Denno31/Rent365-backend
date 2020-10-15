from django.db import models

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
    
