# Generated by Django 3.2.8 on 2021-11-09 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thongke', '0008_tinhhinhcovid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tinhhinhcovid',
            name='homnay',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]