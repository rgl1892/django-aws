from django.db import models

# Create your models here.

class Dataset(models.Model):
    dataset = models.FileField(upload_to='')
    title = models.CharField(max_length=100)
    personal_data = models.CharField(max_length=100)
    export_control = models.CharField(max_length=100)
    national_security = models.CharField(max_length=100)
    company_sensitve = models.CharField(max_length=100)
    business_private = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.title)
