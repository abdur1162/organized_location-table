# Generated by Django 5.1.4 on 2025-02-15 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organized_location', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizedlocation',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='organizedlocation',
            name='anytime_fitness',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='organizedlocation',
            name='appt_file_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='organizedlocation',
            name='concussion',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='organizedlocation',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='organizedlocation',
            name='location_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='organizedlocation',
            name='location_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='organizedlocation',
            name='lon',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='organizedlocation',
            name='nutrition_center',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='organizedlocation',
            name='organization',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='organizedlocation',
            name='pelvic_health',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='organizedlocation',
            name='training_haus',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='organizedlocation',
            name='urgent_care',
            field=models.BooleanField(default=False),
        ),
    ]
