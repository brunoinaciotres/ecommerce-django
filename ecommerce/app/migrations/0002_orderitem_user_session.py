# Generated by Django 5.1.2 on 2024-11-03 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='user_session',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
