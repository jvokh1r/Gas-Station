from django.core.validators import FileExtensionValidator, MinValueValidator
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Station(models.Model):
    name = models.CharField(max_length=255)
    short_text = models.TextField()

    logo = models.ImageField(upload_to='stations/logos/%Y/%m/%d/',
                             blank=True,
                             null=True,
                             validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'gif', 'bmp',
                                                                'tif', 'tiff', 'webp', 'svg', 'heic', 'heif'])])
    rating = models.FloatField(default=0)
    address = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    video = models.FileField(upload_to=f'stations/videos/%Y/%m/%d/', blank=True, null=True)
    comforts = (
        models.CharField(max_length=50)
    )

    def __str__(self):
        return self.name


class StationImage(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='stations/images/%Y/%m/%d/', blank=True, null=True)
    ordering_number = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.ordering_number


class StationWorkTime(models.Model):
    class WeekDay(models.IntegerChoices):
        MONDAY = 0, 'MONDAY'
        TUESDAY = 1, 'TUESDAY'
        WEDNESDAY = 2, 'WEDNESDAY'
        THURSDAY = 3, 'THURSDAY'
        FRIDAY = 4, 'FRIDAY'
        SATURDAY = 5, 'SATURDAY'
        SUNDAY = 6, 'SUNDAY'
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    week_day = models.PositiveSmallIntegerField(choices=WeekDay.choices)

    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = (('station', 'week_day'),)


class OilType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PetrolType(models.Model):
    oil_type = models.ForeignKey(OilType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    mark = models.CharField(max_length=100, blank=True)
    pressure = models.IntegerField(blank=True)

    def __str__(self):
        if self.name:
            return f'{self.oil_type}-{self.name}'
        return self.oil_type


class StationPetrolMark(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    petrol_mark = models.ForeignKey(PetrolType, on_delete=models.SET_NULL)
    number_of_columns = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1)])
    price = models.DecimalField(max_digits=10, decimal_places=1)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.petrol_mark}'


