# Generated by Django 2.2.3 on 2019-07-08 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='id_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_pictures'),
        ),
    ]