# Generated by Django 2.1.4 on 2018-12-17 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='emial',
            field=models.CharField(max_length=32, null=True),
        ),
    ]