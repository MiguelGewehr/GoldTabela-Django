from django.db import models

class Championship(models.Model):
    type = models.CharField(max_length=100, null=False, blank=False)
    year = models.CharField(max_length=20, null=False, blank=False)
    status = models.BooleanField(default=True)
    logo = models.CharField(max_length=100, null=False, blank=False)
    round_count = models.IntegerField(null=False, blank=False)
    matches_per_round = models.IntegerField(null=False, blank=False)
    
    def __str__(self):
        return f"Campeonato [tipo={self.type}]"
    