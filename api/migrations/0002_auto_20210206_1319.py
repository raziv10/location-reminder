# Generated by Django 2.2.11 on 2021-02-06 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.CharField(default='27.70885940768541', max_length=100),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.CharField(default='85.32608415708333', max_length=100),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(default='Demo', max_length=100),
        ),
        migrations.AlterField(
            model_name='location',
            name='task',
            field=models.CharField(default='Explore', max_length=500),
        ),
    ]
