from django.db import models
from manufacturing.models.abstracts import BaseModel


def upload_to(instance, filename):
    return f'{instance._meta.model_name}/{filename}'


class Product(BaseModel):
    category = models.ForeignKey('manufacturing.Category', models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey('users.User', models.CASCADE, null=True, blank=True)

    title = models.CharField(max_length=1000)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(default=0)
    manufacturing_date = models.DateTimeField(null=True, blank=True)
    image = models.FileField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
