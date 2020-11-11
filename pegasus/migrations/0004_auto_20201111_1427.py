# Generated by Django 3.1.1 on 2020-11-11 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pegasus', '0003_scope_is_active'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='role',
            name='default_role_unique',
        ),
        migrations.RenameField(
            model_name='role',
            old_name='default_role',
            new_name='is_default_role',
        ),
        migrations.AddConstraint(
            model_name='role',
            constraint=models.UniqueConstraint(condition=models.Q(is_default_role=True), fields=('is_default_role',), name='is_default_role_unique'),
        ),
    ]
