# Generated by Django 3.0.1 on 2020-05-02 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0002_auto_20200502_0601'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
