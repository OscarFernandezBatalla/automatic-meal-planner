# Generated by Django 4.1 on 2022-09-08 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cuisine_style',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.cuisinestyle'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='difficulty',
            field=models.IntegerField(choices=[(1, 'Muy fácil'), (2, 'Fácil'), (3, 'Media'), (4, 'Difícil'), (5, 'Muy difícil')], null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='dinners',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='fav',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(null=True, to='recipes.ingredient'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='time',
            field=models.IntegerField(null=True),
        ),
    ]
