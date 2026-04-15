from django.db import models


class PriceMaster(models.Model):
    CATEGORY_CHOICES = [
        ('camera', 'Camera'),
        ('cable', 'Cable'),
        ('recorder', 'Recorder'),
        ('channel', 'Channel'),
        ('poe', 'PoE Switch'),
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    item_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.category} - {self.item_type} ({self.price})"