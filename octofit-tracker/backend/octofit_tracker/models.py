from django.db import models

class User(models.Model):
    id = models.BigAutoField(primary_key=True)  # Explicitly define the id field as BigAutoField
    _id = None  # Remove the explicit _id field to avoid conflicts with MongoDB's default behavior
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'octofit_tracker'
        managed = True  # Ensure Django manages the database schema
        db_table = 'user'  # Explicitly set the table name to avoid conflicts

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)

    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    name = models.CharField(max_length=100)
    points = models.IntegerField()

    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_points = models.IntegerField()

    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    duration = models.IntegerField()

    class Meta:
        app_label = 'octofit_tracker'
