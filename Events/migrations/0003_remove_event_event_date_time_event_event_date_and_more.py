# Generated by Django 5.1 on 2024-08-25 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0002_remove_event_rsvp_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_date_time',
        ),
        migrations.AddField(
            model_name='event',
            name='event_date',
            field=models.DateField(default='2024-01-01'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='registration_deadline',
            field=models.DateField(),
        ),
    ]