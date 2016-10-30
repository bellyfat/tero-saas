from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram = models.OneToOneField('notifier.Telegram', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.user)