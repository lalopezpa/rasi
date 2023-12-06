from django.db import models

class MedicalHistoryEntity(models.Model):
    id = models.AutoField(primary_key=True)
    medical_history = models.TextField(null=True, blank=True)
    hash = models.CharField(max_length=64, null=True, blank=True)