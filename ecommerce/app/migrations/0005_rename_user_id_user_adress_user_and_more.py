# Generated by Django 5.1.2 on 2024-11-17 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_user_payment_card_method_user_adress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_adress',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='user_payment_card',
            old_name='user_id',
            new_name='user',
        ),
    ]
