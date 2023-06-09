# Generated by Django 4.1.7 on 2023-03-18 00:43

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scholarship',
            options={'verbose_name_plural': 'Scholarships'},
        ),
        migrations.AddField(
            model_name='scholarship',
            name='acceptance_start_date',
            field=models.DateField(default=django.utils.timezone.now, help_text='Start date to apply for the scholarship'),
        ),
        migrations.AddField(
            model_name='scholarship',
            name='organization',
            field=models.CharField(default='Organization Name', help_text='Organization providing the scholarship', max_length=255),
        ),
        migrations.AddField(
            model_name='scholarship',
            name='quantity',
            field=models.IntegerField(default=1, help_text='Number of scholarships available'),
        ),
        migrations.AddField(
            model_name='scholarship',
            name='winner_announcement_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 2, 0, 43, 9, 841980, tzinfo=datetime.timezone.utc), help_text='Date when the winner will be announced'),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='last_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 17, 0, 43, 9, 841980, tzinfo=datetime.timezone.utc), help_text='Last date to apply for the scholarship'),
        ),
    ]
