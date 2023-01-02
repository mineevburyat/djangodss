# Generated by Django 4.1.4 on 2022-12-28 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sportdss', '0007_object_service_service_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Managment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=60, verbose_name='должность')),
                ('full_name', models.CharField(max_length=60, verbose_name='ФИО')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sportdss.basecategory')),
            ],
            options={
                'verbose_name': 'Руководитель',
                'verbose_name_plural': 'Руководители',
            },
        ),
    ]