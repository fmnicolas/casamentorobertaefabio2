from django.db import models

class Confirmacao(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    attend = models.IntegerField()
    people_count = models.IntegerField()
    message = models.CharField()

    def __str__(self):
        return self.name
