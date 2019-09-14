# Generated by Django 2.2.2 on 2019-09-12 14:48

import GUI.models
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_extensions.db.fields.json


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=1024, null=True)),
                ('bitrix_key', models.CharField(blank=True, default='', max_length=1024, null=True)),
                ('bitrix_domain', models.CharField(blank=True, default='', max_length=1024, null=True)),
                ('amocrm_domain', models.CharField(blank=True, default='', max_length=1024, null=True)),
                ('application_email', models.CharField(blank=True, default='', max_length=1024, null=True)),
                ('application_whatsapp_id', models.CharField(blank=True, default='', max_length=1024, null=True)),
                ('application_will_send', models.BooleanField(default=False)),
                ('whatsapp', models.BooleanField(default=False)),
                ('telegram', models.BooleanField(default=False)),
                ('vk', models.BooleanField(default=False)),
                ('facebook', models.BooleanField(default=False)),
                ('whatsapp_status', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('whatsapp_token', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('whatsapp_instance', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('telegram_token', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('telegram_name', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('vk_group_id', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('vk_group_access_token', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('vk_name', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('facebook_token', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('facebook_group_id', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('facebook_name', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('send_welcome_notif', models.BooleanField(default=False)),
                ('welcome_notif_text', models.CharField(blank=True, default='', max_length=512, null=True)),
                ('welcome_admin_id', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('default_response', models.CharField(blank=True, default='', max_length=4096, null=True)),
                ('welcome_message', models.CharField(blank=True, default='', max_length=4096, null=True)),
                ('payed', models.BooleanField(default=False)),
                ('payed_end_date', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.AutoField(auto_created=True, default=GUI.models.auto_increment_scenario, primary_key=True, serialize=False, unique=True)),
                ('destination', models.CharField(choices=[('', ''), ('broadcast', 'broadcast'), ('autoride', 'autoride'), ('subscribe', 'subscribe'), ('unsubscribe', 'unsubscribe')], default='', max_length=20)),
                ('trigger_text', models.TextField(blank=True, null=True)),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='GUI.Manager')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.CharField(max_length=256, unique=True)),
                ('username', models.CharField(blank=True, default='', max_length=16, null=True)),
                ('user_token', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('utm_source', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('ref', models.IntegerField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='WhatsAppUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=256, null=True)),
                ('name', models.CharField(blank=True, default='', max_length=512, null=True)),
                ('tag', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('mode', models.CharField(blank=True, default='main', max_length=128, null=True)),
                ('data', models.CharField(blank=True, default='main', max_length=4096, null=True)),
                ('user_data', models.CharField(blank=True, default='main', max_length=4096, null=True)),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='GUI.Manager')),
            ],
        ),
        migrations.CreateModel(
            name='WhatsAppReceivedMsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('chat_id', models.CharField(blank=True, max_length=256, null=True)),
                ('user_id', models.CharField(blank=True, max_length=256, null=True)),
                ('sender_name', models.CharField(blank=True, max_length=512, null=True)),
                ('time', models.CharField(blank=True, max_length=256, null=True)),
                ('message_number', models.IntegerField(blank=True, null=True)),
                ('proccessed', models.BooleanField(default=False)),
                ('user_data', models.CharField(blank=True, max_length=512, null=True)),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='GUI.Manager')),
            ],
        ),
        migrations.CreateModel(
            name='WhatsAppDelayMsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.CharField(blank=True, max_length=256, null=True)),
                ('text', models.TextField()),
                ('plan_time', models.IntegerField(blank=True, null=True)),
                ('sent', models.BooleanField(default=False)),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='GUI.Manager')),
            ],
        ),
        migrations.CreateModel(
            name='VkUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=256, null=True)),
                ('name', models.CharField(blank=True, default='', max_length=512, null=True)),
                ('tag', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('mode', models.CharField(blank=True, default='main', max_length=128, null=True)),
                ('data', models.CharField(blank=True, default='main', max_length=4096, null=True)),
                ('user_data', models.CharField(blank=True, default='main', max_length=4096, null=True)),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='GUI.Manager')),
            ],
        ),
        migrations.CreateModel(
            name='VkReceivedMsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.IntegerField(blank=True, null=True)),
                ('text', models.TextField()),
                ('user_id', models.CharField(blank=True, max_length=256, null=True)),
                ('chat_id', models.CharField(blank=True, max_length=256, null=True)),
                ('time', models.IntegerField(blank=True, null=True)),
                ('user_data', models.CharField(blank=True, max_length=512, null=True)),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='GUI.Manager')),
            ],
        ),
        migrations.CreateModel(
            name='VkDelayMsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.CharField(blank=True, max_length=256, null=True)),
                ('text', models.TextField()),
                ('plan_time', models.IntegerField(blank=True, null=True)),
                ('sent', models.BooleanField(default=False)),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='GUI.Manager')),
            ],
        ),
        migrations.CreateModel(
            name='Trigger',
            fields=[
                ('id', models.AutoField(auto_created=True, default=GUI.models.auto_increment, primary_key=True, serialize=False, unique=True)),
                ('caption', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('social', models.CharField(choices=[('telegram', 'telegram'), ('vk', 'vk'), ('whatsapp', 'whatsapp'), ('facebook', 'facebook')], default='telegram', max_length=20)),
                ('keyboard', models.CharField(blank=True, default='{}', max_length=256, null=True)),
                ('messages', django_extensions.db.fields.json.JSONField(blank=True, default={'facebook': [{'keyboard': [], 'text': ''}], 'telegram': [{'keyboard': [], 'text': ''}], 'vk': [{'keyboard': [], 'text': ''}], 'whatsapp': [{'keyboard': [], 'text': ''}]}, null=True)),
                ('scenario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='triggers', to='GUI.Scenario')),
            ],
        ),
        migrations.CreateModel(
            name='TelegramUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=256, null=True)),
                ('name', models.CharField(blank=True, default='', max_length=512, null=True)),
                ('tag', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('mode', models.CharField(blank=True, default='main', max_length=128, null=True)),
                ('data', models.CharField(blank=True, default='main', max_length=4096, null=True)),
                ('user_data', models.CharField(blank=True, default='main', max_length=4096, null=True)),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='GUI.Manager')),
            ],
        ),
        migrations.CreateModel(
            name='TelegramReceivedMsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('chat_id', models.CharField(blank=True, max_length=256, null=True)),
                ('user_id', models.CharField(blank=True, max_length=256, null=True)),
                ('sender_username', models.CharField(blank=True, max_length=512, null=True)),
                ('sender_name', models.CharField(blank=True, max_length=512, null=True)),
                ('chat_title', models.CharField(blank=True, max_length=512, null=True)),
                ('time', models.CharField(blank=True, max_length=256, null=True)),
                ('message_id', models.IntegerField(blank=True, null=True)),
                ('proccessed', models.BooleanField(default=False)),
                ('user_data', models.CharField(blank=True, max_length=512, null=True)),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='GUI.Manager')),
            ],
        ),
        migrations.CreateModel(
            name='TelegramDelayMsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.CharField(blank=True, max_length=256, null=True)),
                ('text', models.TextField()),
                ('plan_time', models.IntegerField(blank=True, null=True)),
                ('sent', models.BooleanField(default=False)),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='GUI.Manager')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('add', 'add'), ('remove', 'remove')], default='add', max_length=20)),
                ('tag_name', models.CharField(default='', max_length=30)),
                ('trigger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='GUI.Trigger')),
            ],
        ),
        migrations.AddField(
            model_name='manager',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='FacebookUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=256, null=True)),
                ('name', models.CharField(blank=True, default='', max_length=512, null=True)),
                ('tag', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('mode', models.CharField(blank=True, default='main', max_length=128, null=True)),
                ('data', models.CharField(blank=True, default='main', max_length=4096, null=True)),
                ('user_data', models.CharField(blank=True, default='main', max_length=4096, null=True)),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='GUI.Manager')),
            ],
        ),
        migrations.CreateModel(
            name='FacebookReceivedMsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.CharField(blank=True, max_length=256, null=True)),
                ('text', models.TextField()),
                ('user_id', models.CharField(blank=True, max_length=256, null=True)),
                ('chat_id', models.CharField(blank=True, max_length=256, null=True)),
                ('time', models.IntegerField(blank=True, null=True)),
                ('user_data', models.CharField(blank=True, max_length=512, null=True)),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='GUI.Manager')),
            ],
        ),
        migrations.CreateModel(
            name='FacebookDelayMsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.CharField(blank=True, max_length=256, null=True)),
                ('text', models.TextField()),
                ('plan_time', models.IntegerField(blank=True, null=True)),
                ('sent', models.BooleanField(default=False)),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='GUI.Manager')),
            ],
        ),
        migrations.CreateModel(
            name='BroadcastMessages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('time', models.IntegerField(blank=True, null=True)),
                ('users_count', models.IntegerField(blank=True, default=0, null=True)),
                ('sent', models.BooleanField(default=False)),
                ('proccessing', models.BooleanField(default=False)),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='GUI.Manager')),
                ('scenario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='GUI.Scenario')),
            ],
        ),
        migrations.CreateModel(
            name='AutoRide',
            fields=[
                ('id', models.AutoField(auto_created=True, default=GUI.models.auto_increment_ride, primary_key=True, serialize=False, unique=True)),
                ('trigger_text', models.TextField(blank=True, null=True)),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='GUI.Manager')),
                ('scenario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='GUI.Scenario')),
            ],
        ),
    ]
