from django.db import models

# Create your models here.
class Resume(models.Model):
    name = models.CharField(max_length=50,blank=False)
    surname = models.CharField(max_length=50, blank=False,default="")
    gender_choice = [
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others')
    ]
    gender = models.CharField(max_length=6, choices=gender_choice, default="")
    birthdate = models.DateField()
    birthplace = models.CharField(max_length=50, blank=False, default="")
    father = models.CharField(max_length=50,blank=False,default="")
    mother = models.CharField(max_length=50,blank=False,default="")
    birthplace_f = models.CharField(max_length=50, blank=False, default="")
    birthplace_m = models.CharField(max_length=50, blank=False, default="")    
    registration_number = models.IntegerField( default="")
    registration_date =  models.DateField(auto_now_add=True)
    issue_date =  models.DateField(default="")    


    def __str__(self):
        return f"{self.name},{self.birthdate},{self.gender},{self.father},{self.mother}"