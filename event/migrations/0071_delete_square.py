# Generated by Django 4.2 on 2024-07-18 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0070_delete_venue_remove_userprofile_question_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Square',
        ),
    ]
