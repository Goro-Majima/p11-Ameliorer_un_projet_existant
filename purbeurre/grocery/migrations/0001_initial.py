# Generated by Django 2.2.4 on 2019-08-21 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('nutrigrade', models.CharField(max_length=1)),
                ('image', models.URLField()),
                ('url', models.URLField()),
                ('nutrient', models.URLField(default='image')),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='grocery.Category')),
            ],
        ),
    ]