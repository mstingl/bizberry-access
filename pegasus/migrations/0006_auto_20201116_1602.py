# Generated by Django 3.1.1 on 2020-11-16 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pegasus', '0005_auto_20201116_1354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='is_default_role',
            new_name='is_default',
        ),
    ]
