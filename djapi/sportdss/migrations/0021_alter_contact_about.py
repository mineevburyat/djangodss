# Generated by Django 4.1.4 on 2022-12-28 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sportdss', '0020_managment_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='about',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sportdss.about', verbose_name='"о нас"'),
        ),
    ]
