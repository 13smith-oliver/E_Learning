# Generated by Django 2.0.2 on 2019-12-09 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companies',
            old_name='businesscode',
            new_name='business_code',
        ),
    ]