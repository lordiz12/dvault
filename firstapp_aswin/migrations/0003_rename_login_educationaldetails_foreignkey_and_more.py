# Generated by Django 5.0 on 2024-04-21 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp_aswin', '0002_educationaldetails_financialdetails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='educationaldetails',
            old_name='login',
            new_name='foreignkey',
        ),
        migrations.RenameField(
            model_name='financialdetails',
            old_name='login',
            new_name='foreignkey',
        ),
    ]