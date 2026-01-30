from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Electronics', 'Electronics'),
        ('Clothing', 'Clothing'),
        ('Food', 'Food'),
        ('Books', 'Books'),
        ('Other', 'Other'),
    ]


    name = models.CharField(max_length=255, blank=False, null=False)   
    sku = models.CharField(max_length=100, unique=True, blank=False, null=False)  
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)  
    stock = models.IntegerField(default=0)
    supplier = models.CharField(max_length=100)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.sku})"


