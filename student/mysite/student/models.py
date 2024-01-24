from django.db import models
from datetime import *

class Student(models.Model):
    name = models.CharField(max_length=255)
    Class = models.PositiveIntegerField(default=1)
    RollNo = models.PositiveIntegerField(default=1)
    Address = models.CharField(max_length=500)
    PhoneNo = models.IntegerField()
    DOB = models.CharField(max_length=12)
    Image = models.CharField(max_length=5000, default="https://dm0qx8t0i9gc9.cloudfront.net/thumbnails/video/qmraJpx/videoblocks-portrait-of-smiling-male-college-student-in-busy-communal-campus-building_s-zrzm3vi_thumbnail-1080_01.png")
    
    def __str__(self):
        return self.name