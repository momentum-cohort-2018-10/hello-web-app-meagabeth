# Generated by Django 2.1.3 on 2018-11-14 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='descriptions',
            new_name='description',
        ),
    ]
