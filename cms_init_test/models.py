from django.db import models


class Contact(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100,blank=True)
    email = models.EmailField()
    phone = models.IntegerField(blank=True)
    body = models.TextField()

    def __str__(self):
        return self.fname

