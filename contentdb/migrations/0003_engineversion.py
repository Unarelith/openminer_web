# Generated by Django 3.0.3 on 2020-03-09 10:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contentdb', '0002_auto_20200226_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='EngineVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=10, unique=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('doc', models.FileField(max_length=1000, upload_to='', verbose_name='File')),
            ],
            options={
                'verbose_name': 'EngineVersion',
                'ordering': ['date'],
            },
        ),
    ]