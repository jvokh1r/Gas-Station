from django.db import models


class Review(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    message = models.CharField(max_length=100)
