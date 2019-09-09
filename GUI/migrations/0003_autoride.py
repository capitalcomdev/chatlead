# Generated by Django 2.2.2 on 2019-08-15 10:23

import GUI.models
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields.json


class Migration(migrations.Migration):

    dependencies = [
        ('GUI', '0002_auto_20190813_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoRide',
            fields=[
                ('id', models.AutoField(auto_created=True, default=GUI.models.auto_increment_ride, primary_key=True, serialize=False, unique=True)),
                ('trigger_text', models.TextField(blank=True, null=True)),
                ('messages', django_extensions.db.fields.json.JSONField(blank=True, default=[], null=True)),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='GUI.Manager')),
            ],
        ),
    ]
