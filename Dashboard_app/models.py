from django.db import models

class DataSource(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    source_url = models.URLField(blank=True, null=True)
    file_path = models.FileField(upload_to='data_files/', blank=True, null=True)

    def __str__(self):
        return self.name

