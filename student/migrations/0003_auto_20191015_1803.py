# Generated by Django 2.2.3 on 2019-10-15 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20190708_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(blank=True, null=True, related_name='students', to='course.Course'),
        ),
    ]