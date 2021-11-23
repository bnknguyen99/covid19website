# Generated by Django 3.2.8 on 2021-11-09 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thongke', '0007_dienbiendich_tieude'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tinhhinhcovid',
            fields=[
                ('idcovid', models.AutoField(primary_key=True, serialize=False)),
                ('tongsoca', models.IntegerField(blank=True, null=True)),
                ('homnay', models.CharField(blank=True, max_length=5, null=True)),
                ('tuvong', models.IntegerField(blank=True, null=True)),
                ('ngaycapnhat', models.ForeignKey(blank=True, db_column='ngaycapnhat', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='thongke.ngaythang', to_field='ngaythang')),
                ('tentinhthanh', models.ForeignKey(blank=True, db_column='tentinhthanh', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='thongke.tinhthanh', to_field='tentinhthanh')),
            ],
            options={
                'db_table': 'tinhhinhcovid',
            },
        ),
    ]
