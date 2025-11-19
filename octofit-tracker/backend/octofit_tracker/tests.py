from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class BasicModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Marvel')
        self.assertEqual(str(team), 'Marvel')

    def test_user_creation(self):
        team = Team.objects.create(name='DC')
        user = User.objects.create(name='Superman', email='superman@dc.com', team=team)
        self.assertEqual(str(user), 'Superman')

    def test_activity_creation(self):
        team = Team.objects.create(name='Marvel')
        user = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=team)
        activity = Activity.objects.create(user=user, type='Running', duration=30, calories=300, date='2025-11-19')
        self.assertEqual(str(activity), 'Running - Iron Man')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups', description='Upper body', difficulty='Easy')
        self.assertEqual(str(workout), 'Pushups')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Marvel')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(str(leaderboard), 'Marvel: 100')
