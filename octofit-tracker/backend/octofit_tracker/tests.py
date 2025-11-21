
from django.test import TestCase
from django.core.management import call_command
from .models import UserProfile, Activity, Team, LeaderboardEntry, WorkoutSuggestion

class PopulateDataTests(TestCase):
    def test_population_command_creates_records(self):
        # Run the management command to populate test data
        call_command("populate_db")

        # Verify that records were created
        profiles = UserProfile.objects.all()
        activities = Activity.objects.all()
        teams = Team.objects.all()
        leaderboard = LeaderboardEntry.objects.all()
        suggestions = WorkoutSuggestion.objects.all()

        self.assertGreaterEqual(profiles.count(), 6, "Expected at least 6 user profiles (Marvel/DC)")
        self.assertGreaterEqual(activities.count(), 6, "Expected at least 6 activities")
        self.assertGreaterEqual(teams.count(), 2, "Expected at least 2 teams (Marvel/DC)")
        self.assertGreaterEqual(leaderboard.count(), 6, "Expected at least 6 leaderboard entries")
        self.assertGreaterEqual(suggestions.count(), 6, "Expected at least 6 workout suggestions")
