from django.db import models

# Create your models here.
class Account(models.Model):
    customer = models.CharField(max_length=220)
    cardNumber = models.CharField(unique=True, max_length=20,null=False)
    pin = models.CharField(max_length=6,null=False)
    balance = models.CharField(max_length=20,null=False)

    def __str__(self):
        return self.customer