# Generated by Django 5.1 on 2024-09-21 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0006_tag_joke_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joke',
            name='tags',
            field=models.ManyToManyField(blank=True, to='jokes.tag'),
        ),
    ]
