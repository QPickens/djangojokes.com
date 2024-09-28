# Generated by Django 5.1 on 2024-09-21 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0005_alter_joke_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='joke',
            name='tags',
            field=models.ManyToManyField(to='jokes.tag'),
        ),
    ]