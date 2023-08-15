# Generated by Django 4.2.4 on 2023-08-15 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
