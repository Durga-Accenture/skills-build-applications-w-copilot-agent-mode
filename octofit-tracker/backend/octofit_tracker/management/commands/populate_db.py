from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User(name='Captain America', email='cap@marvel.com', team=marvel),
            User(name='Thor', email='thor@marvel.com', team=marvel),
            User(name='Superman', email='superman@dc.com', team=dc),
            User(name='Batman', email='batman@dc.com', team=dc),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]
        for user in users:
            user.save()

        # Create workouts
        workouts = [
            Workout(name='Pushups', description='Upper body strength', difficulty='Easy'),
            Workout(name='Running', description='Cardio', difficulty='Medium'),
            Workout(name='Deadlift', description='Full body', difficulty='Hard'),
        ]
        for workout in workouts:
            workout.save()

        # Create activities
        activities = [
            Activity(user=users[0], type='Running', duration=30, calories=300, date=timezone.now().date()),
            Activity(user=users[1], type='Pushups', duration=15, calories=100, date=timezone.now().date()),
            Activity(user=users[3], type='Deadlift', duration=45, calories=400, date=timezone.now().date()),
        ]
        for activity in activities:
            activity.save()

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=500)
        Leaderboard.objects.create(team=dc, points=450)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
