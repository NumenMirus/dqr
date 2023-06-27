from django.db import models

# Create your models here.
class Qrcode(models.Model):
    name = models.CharField(max_length=200)
    internal_url = models.CharField(max_length=500)
    external_url = models.CharField(max_length=500)
    modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='qrcodes/', blank=True, null=True)

    def __str__(self):
        return self.id +' - ' + self.name + ' - ' + self.internal_url + ' - ' + self.external_url + ' - ' + self.modified