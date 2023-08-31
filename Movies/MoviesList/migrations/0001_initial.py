# Generated by Django 4.2.1 on 2023-08-10 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Movie's name", max_length=100)),
                ('date', models.DateField(verbose_name='Date the movie was released')),
            ],
        ),
    ]