
# UserProfile links to Django User
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    def __str__(self):
        return self.display_name or self.user.username

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(UserProfile, related_name="teams", blank=True)
    def __str__(self):
        return self.name

class Activity(models.Model):
    ACTIVITY_CHOICES = [
        ("run", "Run"),
        ("bike", "Biking"),
        ("swim", "Swim"),
        ("walk", "Walk"),
        ("other", "Other"),
    ]
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="activities")
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_CHOICES)
    duration_minutes = models.PositiveIntegerField()
    distance_km = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user} {self.activity_type} {self.timestamp.date()}"

class LeaderboardEntry(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    score = models.FloatField()
    date = models.DateField(auto_now_add=True)
    class Meta:
        ordering = ["-score"]
    def __str__(self):
        return f"{self.user} - {self.score}"

class WorkoutSuggestion(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    recommended_for = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.title
