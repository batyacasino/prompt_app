# Generated by Django 3.0.6 on 2020-06-10 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kosapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='date_of_birth',
            field=models.DateField(default='2000-21-12'),
            preserve_default=False,
        ),
    ]
