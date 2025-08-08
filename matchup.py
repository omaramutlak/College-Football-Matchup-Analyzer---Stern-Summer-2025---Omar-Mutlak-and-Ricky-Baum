from data_fetcher import get_team_stats, get_team_roster
from utils import predict_score, calculate_win_probability, predict_yardage
from visuals import (
    plot_team_comparison,
    plot_team_roster,
    plot_game_prediction,
    plot_predicted_yardage,
)

def simulate_matchup(team1, team2, year):
    stats1 = get_team_stats(team1, year)
    stats2 = get_team_stats(team2, year)
    roster1 = get_team_roster(team1, year)
    roster2 = get_team_roster(team2, year)

    score1, score2 = predict_score(stats1, stats2)
    off_yards1, off_yards2 = predict_yardage(stats1, stats2)
    def_yards1, def_yards2 = off_yards2, off_yards1
    prob1, prob2 = calculate_win_probability(score1, score2)

    winner = "Tie"
    if score1 > score2:
        winner = team1
    elif score2 > score1:
        winner = team2

    plot_game_prediction(team1, team2, score1, score2, prob1, prob2)
    plot_team_comparison(team1, team2, stats1, stats2)
    plot_predicted_yardage(team1, team2, off_yards1, def_yards1, off_yards2, def_yards2)
    plot_team_roster(team1, roster1)
    plot_team_roster(team2, roster2)

    return (
        f"\n{team1} ({prob1}%) vs. {team2} ({prob2}%)\n"
        f"Predicted Score: {team1} {score1} - {score2} {team2} → Winner: {winner}\n"
        f"{team1} - Predicted Offensive Yards: {off_yards1}, Predicted Defensive Yards Allowed: {def_yards1}\n"
        f"{team2} - Predicted Offensive Yards: {off_yards2}, Predicted Defensive Yards Allowed: {def_yards2}"
    )








