from django.db import models

class Cred(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    download = models.URLField(max_length=200)

    def __str__(self):
        return self.title
