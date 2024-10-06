# Generated by Django 5.1 on 2024-10-06 19:33

import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, help_text='Image must be 200px by 200px.', upload_to='avatars/', validators=[users.models.validate_avatar]),
        ),
    ]
