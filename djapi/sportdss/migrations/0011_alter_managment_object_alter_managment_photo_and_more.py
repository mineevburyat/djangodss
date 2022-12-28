# Generated by Django 4.1.4 on 2022-12-28 08:59

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sportdss', '0010_managment_object'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managment',
            name='object',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sportdss.object', verbose_name='Объект'),
        ),
        migrations.AlterField(
            model_name='managment',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='object',
            name='address',
            field=models.CharField(help_text='Адрес совместимый с GeoAPI', max_length=200, verbose_name='адрес'),
        ),
        migrations.AlterField(
            model_name='object',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sportdss.basecategory', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='object',
            name='long_name',
            field=models.CharField(help_text='Ролное официальное имя (не более 250  символов)', max_length=250, verbose_name='официальное имя'),
        ),
        migrations.AlterField(
            model_name='object',
            name='service',
            field=models.ManyToManyField(help_text='выберите доступные на объекте спортивные и прочие услуги, спортивные секции. ', to='sportdss.service'),
        ),
        migrations.AlterField(
            model_name='object',
            name='short_name',
            field=models.CharField(help_text='Короткое имя объекта (не более 10 символов)', max_length=10, verbose_name='краткое имя'),
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='название подраздела')),
                ('descriprion', ckeditor_uploader.fields.RichTextUploadingField(max_length=1000, verbose_name='краткое описание')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sportdss.basecategory')),
            ],
            options={
                'verbose_name': 'Пункт о нас',
                'verbose_name_plural': 'О нас',
            },
        ),
    ]
