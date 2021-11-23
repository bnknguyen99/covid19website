# Generated by Django 3.2.8 on 2021-11-07 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thongke', '0002_auto_20211106_0806'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dienbiendich',
            fields=[
                ('iddienbiendich', models.AutoField(primary_key=True, serialize=False)),
                ('dienbien', models.TextField(db_column='dienbien')),
                ('ngaycapnhat', models.ForeignKey(blank=True, db_column='ngaycapnhat', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='thongke.ngaythang', to_field='ngaythang')),
            ],
            options={
                'db_table': 'dienbiendich',
            },
        ),
    ]
