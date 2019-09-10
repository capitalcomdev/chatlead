# Generated by Django 2.2.2 on 2019-09-05 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GUI', '0015_trigger_keyboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ref',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='utm_source',
            field=models.CharField(blank=True, default='', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='scenario',
            name='destination',
            field=models.CharField(choices=[('', ''), ('broadcast', 'broadcast'), ('autoride', 'autoride'), ('subscribe', 'subscribe'), ('unsubscribe', 'unsubscribe')], default='', max_length=20),
        ),
    ]