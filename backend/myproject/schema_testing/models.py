from django.db import models

# Create your models here.
class AgriculturalParcel(models.Model):
    farm_name = models.CharField(max_length=100)
    plot_name = models.CharField(max_length=100)
