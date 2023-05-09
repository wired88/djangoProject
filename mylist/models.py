from datetime import date
from django.db import models


class ShoppingItem(models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
