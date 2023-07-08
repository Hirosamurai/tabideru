# Generated by Django 4.1.7 on 2023-07-03 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


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
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('last_name', models.CharField(max_length=30, verbose_name='苗字')),
                ('first_name', models.CharField(max_length=30, verbose_name='名前')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='', verbose_name='ホテル写真')),
                ('address', models.CharField(max_length=1000)),
                ('price', models.IntegerField()),
                ('information', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'ホテル',
            },
        ),
        migrations.CreateModel(
            name='Mylist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant', models.CharField(blank=True, max_length=100, null=True)),
                ('list_name', models.CharField(max_length=40)),
                ('hotel', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='tabi.hotel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'マイリスト',
            },
        ),
    ]
