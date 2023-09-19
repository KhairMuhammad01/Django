from django.db import models

# Create your models here.

from django.db import models

class SignupData(models.Model):
    username = models.CharField(max_length=255)
    id_number = models.CharField(max_length=20)
    cr_number = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    resident_id_type = models.CharField(max_length=20)

    def __str__(self):
        return self.username
