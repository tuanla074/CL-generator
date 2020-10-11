from django.db import models

# Create your models here.

class Recruiter(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    title = models.CharField(max_length=20, default="Mr.")
    rec_positon = models.CharField(max_length=500)
    company = models.CharField(max_length=200)
    street = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    province = models.CharField(max_length=500)
    zip_code = models.CharField(max_length=200)
    apply_position = models.CharField(max_length=500)
    dateto = models.CharField(max_length=500, default="Friday, October 8th, 2020")