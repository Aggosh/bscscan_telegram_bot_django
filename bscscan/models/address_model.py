from django.db import models


class Address(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if Address.objects.filter(name=self.name).count() == 0:
            super().save(*args, **kwargs)
