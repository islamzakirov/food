from django.db import models

# Create your models here.
class Food(models.Model):

    name = models.CharField(max_length=300, db_index=True)
    content = models.TextField()
    rasmi = models.ImageField()
    price = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    
    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name


class Aloqa(models.Model):
    name = models.CharField(max_length=100)
    Email = models.EmailField()
    massage = models.TextField(default=0)
    number = models.IntegerField()
    address = models.CharField(max_length=300)

    