# Generated by Django 3.2.16 on 2023-04-03 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_yorum_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yorum',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
