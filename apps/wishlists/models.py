from django.conf import settings
from django.db import models


class WishList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    station = models.ForeignKey('stations.Station', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)


