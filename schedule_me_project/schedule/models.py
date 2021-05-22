from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # This method is to have the title of model print when adding to model through command line.
    def __str__(self):
        return self.title

class Event(models.Model):
    TIME_CHOICES = (
        ('0', '12 AM'), 
        ('1', '1 AM'), ('2', '2 AM'), ('3', '3 AM'), ('4', '4 AM'),
        ('5', '5 AM'), ('6', '6 AM'), ('7', '7 AM'), ('8', '8 AM'),
        ('9', '9 AM'), ('10', '10 AM'), ('11', '11 AM'), ('12', '12 PM'),
        ('13', '1 PM'), ('14', '2 PM'), ('15', '3 PM'), ('16', '4 PM'),
        ('17', '5 PM'), ('18', '6 PM'), ('19', '7 PM'), ('20', '8 PM'),
        ('21', '9 PM'), ('22', '10 PM'), ('23', '11 PM'), ('24', '12 AM'),
    )
    DAY_CHOICES = (
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    )

    title = models.CharField(max_length=50)
    time = models.CharField(max_length=5, choices=TIME_CHOICES)
    day = models.CharField(max_length=9, choices=DAY_CHOICES)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
