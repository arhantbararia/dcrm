from django.db import models

# Create your models here.


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add = True )
    firstName= models.CharField(max_length = 50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=50)


    def __str__(self):
        return (f"{self.firstName} {self.last_name} {self.email}")