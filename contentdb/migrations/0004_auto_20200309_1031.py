# Generated by Django 3.0.3 on 2020-03-09 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contentdb', '0003_engineversion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='engineversion',
            options={'ordering': ['date'], 'verbose_name': 'Engine version'},
        ),
        migrations.RenameField(
            model_name='engineversion',
            old_name='version',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='modversion',
            old_name='version',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='texturepackversion',
            old_name='version',
            new_name='name',
        ),
    ]
