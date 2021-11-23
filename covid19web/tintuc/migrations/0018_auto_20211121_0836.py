# Generated by Django 3.2.8 on 2021-11-21 08:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tintuc', '0017_auto_20211115_1046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='binhluan',
            options={'ordering': ('ngaydang',)},
        ),
        migrations.RemoveField(
            model_name='binhluan',
            name='ngaydangbinhluan',
        ),
        migrations.AddField(
            model_name='binhluan',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='binhluan',
            name='ngaydang',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='binhluan',
            name='baiviet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='tintuc.baiviet'),
        ),
        migrations.AlterModelTable(
            name='binhluan',
            table=None,
        ),
    ]