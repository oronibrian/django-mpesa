# Generated by Django 2.1.7 on 2020-05-29 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesaApp', '0008_payment_success'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_status_message',
            field=models.CharField(default='', max_length=500),
        ),
    ]
