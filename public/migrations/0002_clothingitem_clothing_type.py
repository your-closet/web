# Generated by Django 2.1.7 on 2019-03-23 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothingitem',
            name='clothing_type',
            field=models.CharField(
                blank=True,
                choices=[('top', 'top'), ('bottom', 'bottom'), ('shoe',
                                                                'shoe')],
                default='',
                max_length=255),
        ),
    ]
