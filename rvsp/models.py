from django.db import models

class Confirmacao(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30)
    attend = models.IntegerField()
    people_count = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name
