# Generated by Django 4.1.4 on 2022-12-28 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sportdss', '0011_alter_managment_object_alter_managment_photo_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'пункт "о нас"', 'verbose_name_plural': '"О нас"'},
        ),
        migrations.AddField(
            model_name='managment',
            name='about',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sportdss.about'),
        ),
    ]
