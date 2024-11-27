from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Author(models.Model): 
 name = models.CharField(max_length=255) 
 email = models.EmailField()
 def __str__(self): 
  return self.name

class Article(models.Model): 
 title = models.CharField(max_length=120) 
 description = models.TextField() 
 body = models.TextField() 
 author = models.ForeignKey('Author',null=True, related_name='articles', on_delete=models.CASCADE)
 def __str__(self): 
  return self.title
 
User = get_user_model()
class Capital(models.Model):
    country = models.CharField('country', max_length=150)
    capital_city = models.CharField('capital', max_length=150)
    capital_population = models.IntegerField('population')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
      return self.capital_city