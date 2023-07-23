from django.db import models



class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(null=False, blank=False)
    contact = models.CharField(max_length=25)
    email = models.EmailField()
    address = models.TextField()
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    
