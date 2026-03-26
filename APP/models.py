from django.db import models

# Create your models here.
class review(models.Model):
   your_review=models.TextField()
   
   def __str__(self):
        return self.your_review
    
class registr(models.Model):    
      name=models.CharField(max_length=30, blank=True, null=True)
      email=models.EmailField( blank=True, null=True)
      password=models.CharField(max_length=20, blank=True, null=True)
      status=models.CharField(max_length=20, blank=True, null=True,default='deactivate')
      pin=models.IntegerField(blank=True,null=True)
      

