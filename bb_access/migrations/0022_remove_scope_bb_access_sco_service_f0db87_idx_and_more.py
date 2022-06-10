# Generated by Django 4.0.5 on 2022-06-08 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bb_access', '0021_alter_user_email'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='scope',
            name='bb_access_sco_service_f0db87_idx',
        ),
        migrations.RemoveIndex(
            model_name='scope',
            name='bb_access_sco_service_b0b5d3_idx',
        ),
        migrations.AlterField(
            model_name='role',
            name='included_roles',
            field=models.ManyToManyField(blank=True, related_name='+', to='bb_access.role'),
        ),
        migrations.AddIndex(
            model_name='scope',
            index=models.Index(fields=['service', 'resource', 'action'], name='bb_access_s_service_e4d759_idx'),
        ),
        migrations.AddIndex(
            model_name='scope',
            index=models.Index(fields=['service', 'resource', 'action', 'selector'], name='bb_access_s_service_6abd0f_idx'),
        ),
    ]
