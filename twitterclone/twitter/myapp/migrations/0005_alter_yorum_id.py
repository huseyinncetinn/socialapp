# Generated by Django 3.2.16 on 2023-04-03 09:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_yorum_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yorum',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]