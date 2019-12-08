# Generated by Django 2.0.2 on 2019-12-06 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(choices=[('PUBLIC', 'Public'), ('CORPORATE', 'Corporate'), ('MANAGER', 'Manager')], default='PUBLIC', max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('businesscode', models.CharField(max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='appusers',
            name='company_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.Companies'),
        ),
        migrations.AddField(
            model_name='appusers',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='appusers',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
