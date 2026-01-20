from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    # Link to a Product. If product is deleted, reviews are deleted.
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    # Link to a User. If user is deleted, reviews are deleted.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    # Rating from 1 to 5
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.product.name} by {self.user.username}'