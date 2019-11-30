from django.db import models

# Create your models here.

class Publishing(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    publishing = models.ForeignKey(to='Publishing',on_delete=models.CASCADE)
    price = models.IntegerField(null=True)


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    books = models.ManyToManyField(to='Book')

    # def __str__(self):
    #     return self.name