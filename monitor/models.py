from django.db import models

class Device(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=10, default="Unknown")
    last_checked = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.ip_address})"
