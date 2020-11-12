# Generated by Django 3.1.1 on 2020-11-12 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pegasus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrolerelation',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_rel', to='pegasus.role'),
        ),
        migrations.AlterField(
            model_name='userrolerelation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles_rel', to=settings.AUTH_USER_MODEL),
        ),
    ]
