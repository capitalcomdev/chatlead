# Generated by Django 2.2.2 on 2019-08-16 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GUI', '0003_autoride'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenario',
            name='social',
            field=models.CharField(choices=[('telegram', 'telegram'), ('vk', 'vk'), ('whatsapp', 'whatsapp'), ('facebook', 'facebook')], default='telegram', max_length=20),
        ),
    ]
