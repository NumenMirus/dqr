# Generated by Django 4.2.2 on 2023-06-27 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0003_delete_internalurl_rename_url_qrcode_external_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcode',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='qrcodes/'),
        ),
    ]