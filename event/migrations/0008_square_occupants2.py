# Generated by Django 4.1.7 on 2023-03-28 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_userprofile_xpos_userprofile_ypos'),
    ]

    operations = [
        migrations.AddField(
            model_name='square',
            name='occupants2',
            field=models.ManyToManyField(blank=True, to='event.userprofile'),
        ),
    ]