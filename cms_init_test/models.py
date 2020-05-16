from django.db import models


class Contact(models.Model):
    fname = models.CharField("First Name", max_length=100)
    lname = models.CharField("Last Name", max_length=100,blank=True)
    email = models.EmailField("Email")
    phone = models.IntegerField("Phone Number", blank=True)
    body = models.TextField("What's on your mind?")

    def __str__(self):
        return self.fname

