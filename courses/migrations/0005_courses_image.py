# Generated by Django 3.0.4 on 2020-03-20 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20200320_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='course_pics'),
        ),
    ]