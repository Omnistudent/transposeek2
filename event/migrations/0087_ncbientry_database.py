# Generated by Django 4.2 on 2024-07-27 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0086_ncbientry_has_representative'),
    ]

    operations = [
        migrations.AddField(
            model_name='ncbientry',
            name='database',
            field=models.CharField(default='-1', max_length=120, verbose_name='database'),
        ),
    ]
