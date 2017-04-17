from django.db import models

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)
    rank = models.CharField(max_length=128)

    def __str__(self):
        return "Пользователь: %s с id: %s" % (self.name, self.id)

    class Meta:
        verbose_name = 'users'
        verbose_name_plural = 'user'