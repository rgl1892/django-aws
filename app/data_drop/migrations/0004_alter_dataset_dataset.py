# Generated by Django 4.2.6 on 2023-11-02 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_drop', '0003_dataset_company_sensitve_dataset_dataset_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='dataset',
            field=models.FileField(upload_to='documents/'),
        ),
    ]
