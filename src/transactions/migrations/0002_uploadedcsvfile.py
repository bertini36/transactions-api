# Generated by Django 3.2.2 on 2021-05-07 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedCSVFile',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('filename', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='files/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'uploaded CSV file',
                'verbose_name_plural': 'uploaded CSV files',
            },
        ),
    ]
