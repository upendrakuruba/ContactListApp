from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):

    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    country_code = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    contact_picture = models.URLField(null=True)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name