# Generated by Django 3.0.3 on 2020-03-28 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinamica', '0010_remove_sequencia_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='sequencia',
            name='campos',
            field=models.ManyToManyField(to='dinamica.SEQ_CAMPO'),
        ),
    ]
