# Generated by Django 2.2 on 2020-04-20 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20200418_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='change_password',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=200)),
                ('updatepassword', models.CharField(max_length=200)),
                ('confirmpassword', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='cart',
            name='phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Phone'),
        ),
        migrations.AlterField(
            model_name='review',
            name='phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Phone'),
        ),
    ]
