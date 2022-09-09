# Generated by Django 4.1 on 2022-09-09 17:45

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CuisineStyle',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Difficulty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.fooditem')),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('text', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('image', models.ImageField(default='arroz.jpg', null=True, upload_to='')),
                ('dinners', models.IntegerField()),
                ('time', models.IntegerField()),
                ('cuisine_style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.cuisinestyle')),
                ('difficulty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.difficulty')),
                ('ingredients', models.ManyToManyField(to='recipes.ingredient')),
                ('steps', models.ManyToManyField(to='recipes.step')),
            ],
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.unit')),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='quantity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.quantity'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('bio', models.TextField(null=True)),
                ('avatar', models.ImageField(default='avatar.svg', null=True, upload_to='')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('liked_recipes', models.ManyToManyField(related_name='liked_recipes', to='recipes.recipe')),
                ('own_recipes', models.ManyToManyField(related_name='own_recipes', to='recipes.recipe')),
                ('storage', models.ManyToManyField(related_name='storage', to='recipes.ingredient')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
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
    ]
