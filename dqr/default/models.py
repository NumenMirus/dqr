from django.db import models

# Create your models here.
class Qrcode(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=500)

    def __str__(self):
        return self.id +' - ' + self.name + ' - ' + self.url
    
class InternalUrl(models.Model):
    internal_url = models.CharField(max_length=500)
    external_url = models.CharField(max_length=500)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id +' - ' + self.internal_url + ' - ' + self.external_url + ' - ' + self.modified