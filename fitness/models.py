from django.db import models

class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    points = models.IntegerField()

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    total_points = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
