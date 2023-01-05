# Generated by Django 4.1.4 on 2023-01-04 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sportdss', '0022_document_page_rename_long_name_object_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sportdss.basecategory'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='about',
            field=models.ForeignKey(blank=True, help_text='не выбирать если не надо отображать в пункте меню "о нас - контакты"', null=True, on_delete=django.db.models.deletion.SET_NULL, to='sportdss.about', verbose_name='"о нас"'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='object',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sportdss.object', verbose_name='Объект'),
        ),
        migrations.AlterField(
            model_name='email',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sportdss.contact', verbose_name='Контакт'),
        ),
        migrations.AlterField(
            model_name='managment',
            name='about',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sportdss.about'),
        ),
        migrations.AlterField(
            model_name='managment',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sportdss.contact', verbose_name='Контакты'),
        ),
        migrations.AlterField(
            model_name='managment',
            name='object',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sportdss.object', verbose_name='Объект'),
        ),
        migrations.AlterField(
            model_name='object',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sportdss.basecategory', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sportdss.contact', verbose_name='Контакт'),
        ),
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sportdss.basecategory'),
        ),
        migrations.AlterField(
            model_name='workingmode',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sportdss.contact', verbose_name='Контакт'),
        ),
    ]
