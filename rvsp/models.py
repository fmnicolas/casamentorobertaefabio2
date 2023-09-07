from django.db import models

class Confirmacao(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    attend = models.CharField(max_length=5)
    people_count = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name