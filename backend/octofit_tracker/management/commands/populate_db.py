from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(email='thundergod@mhigh.edu', name='Thor'),
            User(email='metalgeek@mhigh.edu', name='Tony Stark'),
            User(email='zerocool@mhigh.edu', name='Steve Rogers'),
            User(email='crashoverride@mhigh.edu', name='Natasha Romanoff'),
            User(email='sleeptoken@mhigh.edu', name='Bruce Banner'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team1 = Team(name='Blue Team')
        team2 = Team(name='Gold Team')
        team1.save()
        team2.save()
        team1.members.set(users[:3])
        team2.members.set(users[3:])

        # Create activities
        activities = [
            Activity(name='Cycling', points=10),
            Activity(name='Crossfit', points=20),
            Activity(name='Running', points=15),
            Activity(name='Strength Training', points=25),
            Activity(name='Swimming', points=30),
        ]
        Activity.objects.bulk_create(activities)

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
            Workout(user=users[1], activity=activities[1], duration=120),
            Workout(user=users[2], activity=activities[2], duration=90),
            Workout(user=users[3], activity=activities[3], duration=30),
            Workout(user=users[4], activity=activities[4], duration=75),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))