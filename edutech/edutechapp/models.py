from django.db import models

# Create your models here.
role = (
    ("user1", "Staff"),
    ("user2", "Student"),
)
class registration(models.Model):
    
    name = models.CharField(max_length=255,blank=True,null=True)
    lastname = models.CharField(max_length=255,blank=True,null=True)
    gender = models.CharField(max_length=10,blank=True,null=True)
    date_of_birth = models.DateField(null=True)
    phone_number = models.CharField(max_length=255,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    role = models.CharField(max_length=255,blank=True,null=True,choices = role)
    last_login = models.DateTimeField(null=True, blank=True)
    status =models.CharField(max_length = 255,blank=True,null=True, default="active")
    otp =  models.IntegerField(default=0)
    def _str_(self):
        return self.nickname