from django.core.management.base import BaseCommand
from octofit_tracker.models import CustomUser, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB using the host from settings
        mongo_host = settings.DATABASES['default']['CLIENT']['host']
        db_name = settings.DATABASES['default']['NAME']
        client = MongoClient(mongo_host)
        db = client[db_name]

        # Drop existing collections
        db.customuser.drop()
        db.team.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workout.drop()

        # Create users
        users = [
            CustomUser(email='thundergod@mhigh.edu', username='thundergod', password='thundergodpassword'),
            CustomUser(email='metalgeek@mhigh.edu', username='metalgeek', password='metalgeekpassword'),
            CustomUser(email='zerocool@mhigh.edu', username='zerocool', password='zerocoolpassword'),
            CustomUser(email='crashoverride@hmhigh.edu', username='crashoverride', password='crashoverridepassword'),
            CustomUser(email='sleeptoken@mhigh.edu', username='sleeptoken', password='sleeptokenpassword'),
        ]
        CustomUser.objects.bulk_create(users)

        # Re-fetch saved users to get MongoDB _id values
        users = list(CustomUser.objects.all())

        # Create team with members (store usernames or emails)
        team = Team(name='Blue Team', members=[user.username for user in users])
        team.save()

        # Create activities
        activities = [
            Activity(user=users[0].username, activity_type='Cycling', duration=timedelta(hours=1)),
            Activity(user=users[1].username, activity_type='Crossfit', duration=timedelta(hours=2)),
            Activity(user=users[2].username, activity_type='Running', duration=timedelta(hours=1, minutes=30)),
            Activity(user=users[3].username, activity_type='Strength', duration=timedelta(minutes=30)),
            Activity(user=users[4].username, activity_type='Swimming', duration=timedelta(hours=1, minutes=15)),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(user=users[0].username, score=100),
            Leaderboard(user=users[1].username, score=90),
            Leaderboard(user=users[2].username, score=95),
            Leaderboard(user=users[3].username, score=85),
            Leaderboard(user=users[4].username, score=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event'),
            Workout(name='Crossfit', description='Training for a crossfit competition'),
            Workout(name='Running Training', description='Training for a marathon'),
            Workout(name='Strength Training', description='Training for strength'),
            Workout(name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))

