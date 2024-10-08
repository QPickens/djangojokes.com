# Generated by Django 5.1 on 2024-10-06 19:33

import jobs.models
import private_storage.fields
import private_storage.storage.files
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_applicant_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='resume',
            field=private_storage.fields.PrivateFileField(blank=True, help_text='PDFs only', storage=private_storage.storage.files.PrivateFileSystemStorage(), upload_to='resumes', validators=[jobs.models.validate_pdf]),
        ),
    ]
