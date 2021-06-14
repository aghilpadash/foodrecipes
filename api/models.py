from datetime import datetime

from django.db import models


class Recipe(models.Model):
    DIFFICULTY_LEVELS = (
        ('E', 'آسان'),
        ('M', 'متوسط'),
        ('H', 'سخت'),
    )
    name = models.CharField(max_length=120)
    ingredients = models.CharField(max_length=400)
    picture = models.FileField()
    difficulty = models.CharField(choices=DIFFICULTY_LEVELS, max_length=10)
    prep_time = models.PositiveIntegerField()
    prep_guide = models.TextField()
    created_at = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return "Recipe for {}".format(self.name)
