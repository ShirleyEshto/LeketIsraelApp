# Generated by Django 3.2.18 on 2023-04-09 08:18

import LeketIsraelApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LeketIsraelApp', '0003_delete_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50, validators=[LeketIsraelApp.models.validate_password])),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
