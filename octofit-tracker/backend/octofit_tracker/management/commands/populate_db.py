from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import timedelta
from uuid import uuid4

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], int(settings.DATABASES['default']['PORT']))
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.get_collection('octofit_tracker_user').drop()
        db.get_collection('octofit_tracker_team').drop()
        db.get_collection('octofit_tracker_activity').drop()
        db.get_collection('octofit_tracker_leaderboard').drop()
        db.get_collection('octofit_tracker_workout').drop()

        # Create users
        users = [
            User(username='thundergod', email='thundergod@mhigh.edu', password='thundergodpassword'),
            User(username='metalgeek', email='metalgeek@mhigh.edu', password='metalgeekpassword'),
            User(username='zerocool', email='zerocool@mhigh.edu', password='zerocoolpassword'),
            User(username='crashoverride', email='crashoverride@hmhigh.edu', password='crashoverridepassword'),
            User(username='sleeptoken', email='sleeptoken@mhigh.edu', password='sleeptokenpassword'),
        ]
        for index, user in enumerate(users, start=1):
            user._id = index  # Assign a unique numeric value to _id
            self.stdout.write(f"User ID: {user._id}")  # Debug: Print the _id of each user
            user.save()  # Save each user individually to ensure proper ID generation

        # Refresh users from the database to ensure IDs are properly initialized
        users = list(User.objects.all())
        for user in users:
            self.stdout.write(f"Refreshed User ID: {user.id}, Username: {user.username}")  # Debug: Verify user state after refresh

        # Convert ObjectId to integer before saving users
        for user in users:
            user.id = int(str(user.id), 16) if isinstance(user.id, ObjectId) else user.id  # Convert ObjectId to integer
            user.save()  # Ensure each user is saved to the database before adding to the team

        # Reset the id field for users before saving them to ensure proper handling by Django
        for user in users:
            user.id = None  # Reset the id field to let Django handle it
            user.save()  # Save the user to ensure proper id assignment

        # Explicitly set the id field to the primary key value for users before saving them
        for user in users:
            user.id = user.pk  # Explicitly set the id field to the primary key value
            user.save()  # Save the user to ensure proper id assignment

        # Explicitly convert ObjectId to integer for the id field before saving users
        for user in users:
            user.id = int(str(user.pk), 16) if isinstance(user.pk, ObjectId) else user.pk  # Convert ObjectId to integer
            user.save()  # Save the user to ensure proper id assignment

        # Create teams
        team = Team(name='Blue Team')
        team.save()  # Explicitly save the team instance before adding members
        self.stdout.write(f"Team ID: {team.id}")
        for user in users:
            self.stdout.write(f"Adding User ID: {user.id} to Team ID: {team.id}")
            team.members.add(user)  # Add each member individually to ensure proper handling

        # Create activities
        activities = [
            Activity(name='Cycling', points=100),
            Activity(name='Crossfit', points=90),
            Activity(name='Running', points=95),
            Activity(name='Strength', points=85),
            Activity(name='Swimming', points=80),
        ]
        Activity.objects.bulk_create(activities)

        # Save activities before creating workouts
        for activity in activities:
            activity.save()  # Ensure each activity is saved to the database

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(user=users[0], total_points=100),
            Leaderboard(user=users[1], total_points=90),
            Leaderboard(user=users[2], total_points=95),
            Leaderboard(user=users[3], total_points=85),
            Leaderboard(user=users[4], total_points=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(user=users[0], activity=activities[0], duration=60),
            Workout(user=users[1], activity=activities[1], duration=45),
            Workout(user=users[2], activity=activities[2], duration=50),
            Workout(user=users[3], activity=activities[3], duration=40),
            Workout(user=users[4], activity=activities[4], duration=30),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))