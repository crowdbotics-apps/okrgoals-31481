from django.conf import settings
from django.db import models


class Objectives(models.Model):
    "Generated Model"
    title = models.TextField()
    pct = models.BigIntegerField()


class KeyResults(models.Model):
    "Generated Model"
    title = models.TextField()
    pct = models.BigIntegerField()
    objective = models.ForeignKey(
        "home.Objectives",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="keyresults_objective",
    )
