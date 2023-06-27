from io import BytesIO
import os
from django.db import models
import qrcode
from dqr.settings import MEDIA_URL
from django.core.files import File

# Create your models here.
class Qrcode(models.Model):
    name = models.CharField(max_length=200)
    internal_url = models.CharField(max_length=500)
    external_url = models.CharField(max_length=500)
    modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='qrcodes/', blank=True)

    def make_qrcode(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data("http://michaelbasta.it/dqr/" + self.internal_url)
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color="black", back_color="transparent")
        image_url = os.path.join(MEDIA_URL, 'qrcodes/', self.internal_url + '.png')

        # Create a BytesIO buffer to hold the image data
        buffer = BytesIO()
        qr_image.save(buffer)
        buffer.seek(0)

        # Save the image to the database
        self.image.save(self.internal_url + '.png', File(buffer))
        print(self.image.url)
        print(self.image.path)
        self.save()

    def __str__(self):
        return self.id +' - ' + self.name + ' - ' + self.internal_url + ' - ' + self.external_url + ' - ' + self.modified