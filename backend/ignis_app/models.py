from django.db import models

class User(models.Model):
    email=models.EmailField(max_length=50,unique=True,blank=False,null=False)
    password=models.CharField(max_length=70,blank=False,null=False)
    def __str__(self):
        return self.email
    
class Events(models.Model):
    user=models.ForeignKey(User,null=False,on_delete=models.CASCADE)
    event_name=models.CharField(max_length=200,blank=False)
    time=models.CharField(max_length=10,blank=False)
    location=models.CharField(max_length=100,blank=False)
    image=models.URLField(blank=False)
    date=models.CharField(max_length=15,blank=False)
    def __str__(self):
        return self.event_name
    
class Likes(models.Model):
    user=models.ForeignKey(User,null=False,on_delete=models.CASCADE)
    likes = models.OneToOneField(Events,on_delete=models.CASCADE,unique=True)
    def __str__(self):
        return self.likes.event_name



