# Generated by Django 5.1.1 on 2024-10-15 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('sort_description', models.CharField(max_length=500)),
            ],
        ),
    ]
