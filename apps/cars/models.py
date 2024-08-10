from django.db import models


class UserCar(models.Model):
    class CarCategory(models.IntegerChoices):
        Sedan = 0
        Hatchback = 1
        Kupe = 2
        Convertible = 3
        Crossover = 4
        SUV = 5
        Pickup = 6
        Minivan = 7
        Mikroavtobus = 8
        
    user = models.ForeignKey('apps.users.CustomUser', on_delete=models.CASCADE)
    number = models.CharField(max_length=11, unique=True)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    category = models.


