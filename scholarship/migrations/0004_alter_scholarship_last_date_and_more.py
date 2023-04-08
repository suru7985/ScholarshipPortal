# Generated by Django 4.1.7 on 2023-04-07 13:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0003_scholarship_amount_alter_scholarship_last_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarship',
            name='last_date',
            field=models.DateField(default=datetime.datetime(2023, 5, 7, 13, 14, 3, 751808, tzinfo=datetime.timezone.utc), help_text='Last date to apply for the scholarship'),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='winner_announcement_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 22, 13, 14, 3, 751808, tzinfo=datetime.timezone.utc), help_text='Date when the winner will be announced'),
        ),
    ]