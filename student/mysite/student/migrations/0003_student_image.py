# Generated by Django 5.0.1 on 2024-01-23 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student_dob_alter_student_class_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Image',
            field=models.CharField(default='https://dm0qx8t0i9gc9.cloudfront.net/thumbnails/video/qmraJpx/videoblocks-portrait-of-smiling-male-college-student-in-busy-communal-campus-building_s-zrzm3vi_thumbnail-1080_01.png', max_length=5000),
        ),
    ]
