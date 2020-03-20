from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Teachers(models.Model):
    user_id = models.OneToOneField(User ,on_delete=models.CASCADE)
    num_of_courses = models.IntegerField(default=0)
    category = models.CharField(max_length=100,default="Enter Your Interests")
    age = models.IntegerField(default=0)
    image = models.ImageField(default="default-user.jpg",upload_to="user_pics")    

    def __str__(self):
        return self.user_id.username

class Courses(models.Model):
    teacher_id = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    avg_rating = models.IntegerField(default=0)
    price = models.IntegerField(null=False)
    brief_desc = models.TextField()
    table_of_content = models.TextField(default="Enter the Topics which will be taught")
    image = models.ImageField(default="default.jpg",upload_to="course_pics")
    def __str__(self):
        return self.title

class Users_Extended(models.Model):
    user_id = models.OneToOneField(User ,on_delete=models.CASCADE)
    courses_enrolled = models.ForeignKey(Courses, on_delete=models.CASCADE)
    def __str__(self):
        return self.user_id.username

class Comments(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Courses ,on_delete=models.CASCADE)
    body = models.CharField(max_length=100)
    rating = models.IntegerField()

class Videos(models.Model):
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    # only video link