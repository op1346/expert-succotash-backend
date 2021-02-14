from django.conf import settings
from django.db import models
from django.utils import timezone

class Company(models.Model):
    company_name = models.CHARFIELD(max_length=200)
    category =
    subcategory =
    company_url =
    company_description = models.Textfield()
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
      self.save()

    def __str__(self):
      return self.company_name

class Product(models.Model):
    product_name =
    product_description =
    category =
    created_date =


