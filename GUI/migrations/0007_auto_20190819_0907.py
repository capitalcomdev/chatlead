# Generated by Django 2.2.2 on 2019-08-19 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GUI', '0006_auto_20190816_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='facebookreceivedmsg',
            name='user_data',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='telegramreceivedmsg',
            name='user_data',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='vkreceivedmsg',
            name='user_data',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='whatsappreceivedmsg',
            name='user_data',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]