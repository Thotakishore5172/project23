# Generated by Django 4.2.7 on 2023-12-11 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpage',
            name='email',
            field=models.EmailField(default='india@gmail.com', max_length=254),
        ),
    ]
