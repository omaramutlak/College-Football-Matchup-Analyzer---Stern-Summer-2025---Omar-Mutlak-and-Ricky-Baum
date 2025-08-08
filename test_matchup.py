import pytest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from matchup import simulate_matchup
from visuals import plot_team_roster


def test_plot_team_roster_handles_data(monkeypatch):
    monkeypatch.setattr("visuals.go.Figure.show", lambda self: None)
    roster = [
        {"lastName": "Doe", "position": "QB", "jersey": 12},
        {"lastName": "Smith", "position": "RB", "jersey": 5},
    ]

    plot_team_roster("Test Team", roster)


def test_simulate_matchup_with_rosters(monkeypatch):
    def mock_get_team_stats(team, year):
        return [
            {"statName": "totalYards", "statValue": 500},
            {"statName": "totalYardsOpponent", "statValue": 300},
            {"statName": "games", "statValue": 10},
        ]

    def mock_get_team_roster(team, year):
        return [
            {"lastName": "Player", "position": "QB", "jersey": 1}
        ]

    plot_calls = []

    def mock_plot_team_roster(team, roster):
        plot_calls.append((team, roster))

    monkeypatch.setattr("matchup.get_team_stats", mock_get_team_stats)
    monkeypatch.setattr("matchup.get_team_roster", mock_get_team_roster)
    monkeypatch.setattr("matchup.plot_team_comparison", lambda *args, **kwargs: None)
    monkeypatch.setattr("matchup.plot_team_roster", mock_plot_team_roster)
    monkeypatch.setattr("matchup.plot_game_prediction", lambda *args, **kwargs: None)
    monkeypatch.setattr("matchup.plot_predicted_yardage", lambda *args, **kwargs: None)

    result = simulate_matchup("Team A", "Team B", 2023)
    assert "Winner" in result
    assert len(plot_calls) == 2
