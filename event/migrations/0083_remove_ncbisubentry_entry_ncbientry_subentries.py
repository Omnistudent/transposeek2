# Generated by Django 4.2 on 2024-07-21 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0082_ncbisubentry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ncbisubentry',
            name='entry',
        ),
        migrations.AddField(
            model_name='ncbientry',
            name='subentries',
            field=models.ManyToManyField(blank=True, to='event.ncbisubentry'),
        ),
    ]