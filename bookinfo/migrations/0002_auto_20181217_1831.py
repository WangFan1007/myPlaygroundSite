# Generated by Django 2.1.4 on 2018-12-17 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookinfo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publisher_id',
            new_name='publisher',
        ),
    ]