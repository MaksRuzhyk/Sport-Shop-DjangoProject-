from django.db import models
from django.shortcuts import reverse

class Product(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    info = models.TextField(blank=True)
    price = models.IntegerField()
    categories = models.ManyToManyField('Category',blank=True, related_name='products')
    image = models.ImageField(upload_to='images/', default='images/no_image.jpg')

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('product_detail_url', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-price']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    def __str__(self):
        return self.title

    def get_absolute_urls(self):
        return reverse('category_detail_url', kwargs={'pk': self.pk})

class Order(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
