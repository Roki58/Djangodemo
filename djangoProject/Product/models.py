from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Fixed decimal_places typo
    stock = models.IntegerField()
    supplier = models.CharField(max_length=255, default='supplier-1')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Changed to auto_now to update on every save

    def __str__(self):
        return self.name
