# Generated by Django 2.0.2 on 2019-12-10 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20191209_1115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appusers',
            old_name='company_id',
            new_name='company',
        ),
    ]