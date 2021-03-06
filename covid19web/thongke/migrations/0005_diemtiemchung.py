# Generated by Django 3.2.8 on 2021-11-08 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thongke', '0004_tinhhinhvaccine_tinhthanh'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diemtiemchung',
            fields=[
                ('iddiadiem', models.AutoField(primary_key=True, serialize=False)),
                ('tendiemtiem', models.CharField(max_length=100)),
                ('sonha', models.CharField(blank=True, max_length=100, null=True)),
                ('xaphuong', models.CharField(blank=True, max_length=100, null=True)),
                ('nguoiquanly', models.CharField(blank=True, max_length=50, null=True)),
                ('sobantiem', models.IntegerField(blank=True, null=True)),
                ('tentinhthanh', models.ForeignKey(blank=True, db_column='tentinhthanh', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='thongke.tinhthanh', to_field='tentinhthanh')),
            ],
            options={
                'db_table': 'diemtiemchung',
            },
        ),
    ]
