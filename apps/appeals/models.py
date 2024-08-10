from django.db import models


class Appeal(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    message = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=17)

    def __str__(self):
        return self.user
