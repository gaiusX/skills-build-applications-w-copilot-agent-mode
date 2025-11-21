from django.test import TestCase
from django.core.management import call_command
from .models import UserProfile, Activity, Team, LeaderboardEntry, WorkoutSuggestion


class PopulateDataTests(TestCase):
    def test_population_command_creates_records(self):
        # Run the management command to populate test data
        call_command("populate_test_data")

        # Verify that records were created
        profiles = UserProfile.objects.all()
        activities = Activity.objects.all()
        teams = Team.objects.all()
        leaderboard = LeaderboardEntry.objects.all()
        suggestions = WorkoutSuggestion.objects.all()

        self.assertGreaterEqual(profiles.count(), 3, "Expected at least 3 user profiles")
        self.assertGreaterEqual(activities.count(), 3, "Expected at least 3 activities")
        self.assertGreaterEqual(teams.count(), 1, "Expected at least 1 team")
        self.assertGreaterEqual(leaderboard.count(), 3, "Expected at least 3 leaderboard entries")
        self.assertGreaterEqual(suggestions.count(), 3, "Expected at least 3 workout suggestions")
