from django.db import models


# Create your models here.
 
class wings(models.Model):
    add=models.CharField(max_length=1000)
    point=models.TextField()
    description=models.TextField()
    
    def _str_(self):
        return self.add,
        

    
    