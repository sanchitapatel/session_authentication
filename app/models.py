from django.db import models

# Create your models here.
from django.db import models
  
class MovieModel(models.Model):
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    class Meta:
        verbose_name_plural  = "MovieModel"
        verbose_name = "Movie"
    def __str__(self):
        return self.title
    

# class StudentModel(models.Model):
#     name = models.CharField(max_length = 200)
#     email = models.EmailField()
#     city = models.CharField(max_length=100)
#     class Meta:
#         verbose_name_plural  = "Student"
        
    # def __str__(self):
        # return self.name