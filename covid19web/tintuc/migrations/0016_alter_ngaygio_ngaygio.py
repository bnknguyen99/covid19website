# Generated by Django 3.2.8 on 2021-11-14 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tintuc', '0015_alter_ngaygio_ngaygio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngaygio',
            name='ngaygio',
            field=models.DateTimeField(blank=True, null=True, unique=True),
        ),
    ]