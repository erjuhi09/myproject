# Generated by Django 2.2 on 2020-04-18 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20200418_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Phone'),
        ),
    ]
