from django.core.validators import MinValueValidator
from django.db import models


class Booking(models.Model):
    car = models.ForeignKey('apps.cars.UserCar', on_delete=models.CASCADE)
    station = models.ForeignKey('apps.stations.Station', on_delete=models.CASCADE)
    petrol_mark = models.ForeignKey('apps.stations.PetrolType', on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    datetime = models.DateTimeField()
    minutes = models.IntegerField()

    def __str__(self):
        return self.car

