# Generated by Django 3.2.8 on 2021-11-06 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thongke', '0002_auto_20211106_0806'),
        ('tintuc', '0002_alter_baiviet_ngaydangbaiviet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ngaygio',
            fields=[
                ('idngay', models.AutoField(primary_key=True, serialize=False)),
                ('ngaygio', models.DateTimeField(blank=True, null=True, unique=True)),
            ],
            options={
                'db_table': 'ngaygio',
            },
        ),
        migrations.AlterField(
            model_name='baiviet',
            name='ngaydangbaiviet',
            field=models.OneToOneField(blank=True, db_column='ngayDangBaiViet', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tintuc.ngaygio'),
        ),
        migrations.DeleteModel(
            name='Ngaythang',
        ),
    ]
