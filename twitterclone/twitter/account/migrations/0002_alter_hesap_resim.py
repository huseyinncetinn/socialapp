# Generated by Django 3.2.16 on 2023-03-23 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hesap',
            name='resim',
            field=models.FileField(blank=True, default='profil_pic/default.jpg', upload_to='profil_pic/'),
        ),
    ]
