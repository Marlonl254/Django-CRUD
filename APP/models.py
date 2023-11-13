from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    course = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.IntegerField(null=False)
    image = models.ImageField(upload_to="uploads/images")
    
    def __str__(self):
        return self.name


