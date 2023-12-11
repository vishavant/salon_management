# Generated by Django 4.2 on 2023-12-11 06:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0004_payment_assigned_person_payment_payment_mode_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='date',
        ),
        migrations.AddField(
            model_name='booking',
            name='assigned_person',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='service_amount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
