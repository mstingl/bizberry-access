# Generated by Django 3.1.1 on 2020-11-11 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pegasus', '0004_auto_20201111_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='included_roles',
        ),
    ]
