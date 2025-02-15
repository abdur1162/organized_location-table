from django.db import models

class OrganizedLocation(models.Model):
    appt_file_name = models.CharField(max_length=255, blank=True, null=True)
    location_number = models.CharField(max_length=100, blank=True, null=True)
    location_name = models.CharField(max_length=255, blank=True, null=True)
    organization = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    active_status = models.CharField(max_length=50, blank=True, null=True)
    pelvic_health = models.CharField(max_length=10, blank=True, null=True)  # Yes/No stored as text
    training_haus = models.CharField(max_length=10, blank=True, null=True)
    anytime_fitness = models.CharField(max_length=10, blank=True, null=True)
    concussion = models.CharField(max_length=10, blank=True, null=True)
    urgent_care = models.CharField(max_length=10, blank=True, null=True)
    nutrition_center = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.location_name or "Unknown Location"
