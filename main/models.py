# main/models.py
from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)  # 음식 이름
    expiration_date = models.DateField()  # 유통기한

    def __str__(self):
        return self.name
