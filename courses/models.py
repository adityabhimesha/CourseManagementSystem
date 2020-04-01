from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Teachers(models.Model):
    user_id = models.OneToOneField(User ,on_delete=models.CASCADE)
    num_of_courses = models.IntegerField(default=0)
    category = models.CharField(max_length=30,default="Enter Your Interests")
    age = models.IntegerField(default=0)
    profile_pic = models.ImageField(default="user_pics/default-user.png",upload_to="user_pics")    

    def __str__(self):
        return self.user_id.username

class Courses(models.Model):
    teacher_id = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    avg_rating = models.IntegerField(default=0)
    price = models.IntegerField(null=False)
    brief_desc = models.TextField()
    table_of_content = models.TextField(default="Enter the Topics which will be taught")
    image = models.ImageField(default="course_pics/default.jpg",upload_to="course_pics")

    def __str__(self):
        return self.title

class Users_Extended(models.Model):
    user_id = models.ForeignKey(User ,on_delete=models.CASCADE)
    courses_enrolled = models.ForeignKey(Courses, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user_id.username

class Videos(models.Model):
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    video_number = models.IntegerField()
    thumbnail = models.ImageField(default="video_pics/default.jpg",upload_to="video_pics")
    desc = models.CharField(max_length=500)
    video_file= models.FileField(upload_to='course_videos/', default="course_videos/life_hacks.mp4")
    
    def __str__(self):
        return self.name

class Comments(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.ForeignKey(Videos ,default=24, on_delete=models.CASCADE)
    body = models.CharField(max_length=100)
    rating = models.IntegerField()

    def __str__(self):
        return self.body