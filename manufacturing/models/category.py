from manufacturing.models.abstracts import BaseModel
from django.db import models


class Category(BaseModel):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title
