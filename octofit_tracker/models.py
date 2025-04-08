from djongo import models

class CustomUser(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.JSONField()

class Activity(models.Model):
    user = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    duration = models.DurationField()

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    score = models.IntegerField()

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
