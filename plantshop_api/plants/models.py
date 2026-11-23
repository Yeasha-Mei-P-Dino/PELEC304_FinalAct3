from django.db import models


class Plant(models.Model):
    CARE_CHOICES = [
        ("Easy", "Easy"),
        ("Moderate", "Moderate"),
        ("Expert", "Expert"),
    ]

    name = models.CharField(max_length=120)
    scientific_name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    care_level = models.CharField(max_length=20, choices=CARE_CHOICES, default="Easy")

    def __str__(self):
        return f"{self.name} ({self.scientific_name})"