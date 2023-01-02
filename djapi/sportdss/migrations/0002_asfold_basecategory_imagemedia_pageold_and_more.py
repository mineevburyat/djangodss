# Generated by Django 4.1.4 on 2022-12-27 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportdss', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ASFOld',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=150)),
                ('short_desc', models.CharField(max_length=200)),
                ('children_view', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Карточка страницы',
                'verbose_name_plural': 'Карточки страниц',
            },
        ),
        migrations.CreateModel(
            name='BaseCategory',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='id категории')),
                ('title', models.CharField(max_length=25, verbose_name='название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='ImageMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.CharField(max_length=100)),
                ('medium', models.CharField(max_length=100)),
                ('large', models.CharField(max_length=100)),
                ('full', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Медиа ссылка',
                'verbose_name_plural': 'Медиа ссылки',
            },
        ),
        migrations.CreateModel(
            name='PageOld',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('slug', models.CharField(max_length=20, verbose_name='slug')),
                ('excerpt', models.CharField(max_length=250, verbose_name='контакты')),
                ('parent', models.PositiveIntegerField(verbose_name='id родительской категории')),
                ('content', models.CharField(max_length=1000, verbose_name='содержимое')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
            },
        ),
        migrations.DeleteModel(
            name='WorkDay',
        ),
    ]