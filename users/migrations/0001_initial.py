# Generated by Django 4.2.5 on 2023-09-05 21:30

from django.db import migrations, models
import django.utils.timezone
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('avatar', models.ImageField(default='avatar.png', upload_to='')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-date_joined'],
            },
            bases=(models.Model, PermissionError),
            managers=[
                ('objects', users.models.CustomUsersManager()),
            ],
        ),
    ]
