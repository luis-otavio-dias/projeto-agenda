# Generated by Django 5.1.6 on 2025-03-01 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_alter_category_options_contact_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='pictures',
            new_name='picture',
        ),
    ]
