from django.db import models

# Create your models here.
class Club(models.Model):
    club_number = models.IntegerField()
    name = models.CharField(max_length=4)
    stree = models.CharField(max_length = 50)
    street_num = models.IntegerField()
    city = models.CharField(max_length=50)
    post_code = models.CharField(max_length=8)
    landline_no = models.CharField(max_length=15)
    mobile_no = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class Representative(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dob = models.DateField()
