# Generated by Django 3.2.8 on 2021-11-08 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thongke', '0005_diemtiemchung'),
    ]

    operations = [
        migrations.AddField(
            model_name='diemtiemchung',
            name='quanhuyen',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
