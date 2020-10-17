from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Sales(models.Model):
    location = models.CharField(max_length=15)
    min_customer = models.CharField(max_length=8)
    max_customer = models.CharField(max_length=8)
    avg_sales = models.CharField(max_length=8)
    manager = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.location