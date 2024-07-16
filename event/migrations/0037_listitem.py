# Generated by Django 4.2 on 2023-06-24 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0036_question_area4_question_area5_alter_question_area3'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_checked', models.BooleanField(default=False)),
                ('size', models.IntegerField(default=-1, verbose_name='size')),
            ],
        ),
    ]