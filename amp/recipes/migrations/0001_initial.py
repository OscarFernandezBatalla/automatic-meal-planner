# Generated by Django 4.1 on 2022-08-27 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CuisineStyle',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('dinners', models.IntegerField()),
                ('difficulty', models.IntegerField(choices=[(1, 'Muy fácil'), (2, 'Fácil'), (3, 'Media'), (4, 'Difícil'), (5, 'Muy difícil')])),
                ('cuisine_style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.cuisinestyle')),
                ('ingredients', models.ManyToManyField(to='recipes.ingredient')),
            ],
        ),
    ]
