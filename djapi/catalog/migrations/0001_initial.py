# Generated by Django 4.1.4 on 2022-12-21 17:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('middle_name', models.CharField(blank=True, max_length=100, verbose_name='Второе имя (среднее)')),
                ('patronymic', models.CharField(blank=True, max_length=100, verbose_name='Отчество')),
                ('style_name', models.CharField(blank=True, choices=[('en', 'английский'), ('ru', 'русский'), ('ch', 'китайский'), ('ar', 'арабский')], default='ru', help_text='выберите стиль написания полного имени автора', max_length=2, verbose_name='стиль написания имени')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='дата рождения')),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='дата смерти')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название книги')),
                ('summary', models.TextField(help_text='Введите краткое описание книги', max_length=1000)),
                ('isbn', models.CharField(help_text='13 символов <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13, verbose_name='ISBN')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.author')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите жанр книги (такие как Научная фантастика, французкая поэзия и пр.)', max_length=200, verbose_name='Имя жанра')),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='уникальный индентификатор этой книги в библиотеке', primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=200)),
                ('due_back', models.DateField(blank=True, null=True, verbose_name='Дата возврата')),
                ('status', models.CharField(blank=True, choices=[('m', 'на техобслуживании'), ('o', 'на руках'), ('a', 'доступен'), ('r', 'зарезервирован')], default='m', help_text='выберите статус книги', max_length=1, verbose_name='статус')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.book')),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Выберите жанры для этой книги', to='catalog.genre'),
        ),
    ]
