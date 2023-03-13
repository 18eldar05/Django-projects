# Generated by Django 4.0.5 on 2023-02-21 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estiem', '0005_category_slug_estiem_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='estiem',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='estiem.category', verbose_name='Категории'),
        ),
        migrations.AlterField(
            model_name='estiem',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='URL'),
        ),
    ]
