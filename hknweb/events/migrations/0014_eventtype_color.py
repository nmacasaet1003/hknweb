# Generated by Django 2.1.11 on 2019-11-15 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20191008_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventtype',
            name='color',
            field=models.CharField(default='#0072c1', max_length=7),
        ),
    ]