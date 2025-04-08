from django.test import TestCase
from .models import Team, Activity, Leaderboard, Workout
from octofit_tracker.models import User as OctofitUser

class UserModelTest(TestCase):
    def test_create_user(self):
        user = OctofitUser.objects.create(email="test@example.com", name="Test User")
        self.assertEqual(user.email, "test@example.com")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Team A")
        self.assertEqual(team.name, "Team A")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(name="Running", points=10)
        self.assertEqual(activity.points, 10)

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard_entry(self):
        user = OctofitUser.objects.create(email="leader@example.com", name="Leader User")
        leaderboard = Leaderboard.objects.create(user=user, total_points=100)
        self.assertEqual(leaderboard.total_points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = OctofitUser.objects.create(email="workout@example.com", name="Workout User")
        activity = Activity.objects.create(name="Cycling", points=20)
        workout = Workout.objects.create(user=user, activity=activity, duration=60)
        self.assertEqual(workout.duration, 60)
