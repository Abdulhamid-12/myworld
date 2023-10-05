# Generated by Django 4.2.1 on 2023-10-04 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(help_text="Contributor's email", max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='MovieContributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('ACTOR', 'Actor'), ('DIRECTOR', 'Director')], max_length=20, verbose_name="Contributor's role in this movie")),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MoviesList.contributor')),
            ],
        ),
        migrations.CreateModel(
            name='Movies_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Movie's name", max_length=100)),
                ('date', models.DateField(verbose_name='Date the movie was released')),
                ('contributors', models.ManyToManyField(through='MoviesList.MovieContributor', to='MoviesList.contributor')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Publisher name', max_length=50)),
                ('website', models.URLField(help_text='publisher website')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('rating', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('movie', models.ForeignKey(help_text='Reviewed movie', on_delete=django.db.models.deletion.CASCADE, to='MoviesList.movies_info')),
            ],
        ),
        migrations.AddField(
            model_name='movies_info',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MoviesList.publisher'),
        ),
        migrations.AddField(
            model_name='moviecontributor',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MoviesList.movies_info'),
        ),
    ]
