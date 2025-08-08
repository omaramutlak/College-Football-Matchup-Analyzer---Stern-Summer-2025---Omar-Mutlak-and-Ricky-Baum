import plotly.graph_objects as go
from utils import extract_stat

def plot_team_comparison(team1, team2, stats1, stats2):
    team1_off_yards = extract_stat(stats1, "totalYards")
    team2_off_yards = extract_stat(stats2, "totalYards")

    team1_def_yards = extract_stat(stats1, "totalYardsOpponent")
    team2_def_yards = extract_stat(stats2, "totalYardsOpponent")

    categories = ["Offensive Yards", "Defensive Yards Allowed"]
    team1_values = [team1_off_yards, team1_def_yards]
    team2_values = [team2_off_yards, team2_def_yards]

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=categories,
        y=team1_values,
        name=team1
    ))

    fig.add_trace(go.Bar(
        x=categories,
        y=team2_values,
        name=team2
    ))

    fig.update_layout(
        title=f"{team1} vs {team2} - Season Yardage Comparison",
        xaxis_title="Category",
        yaxis_title="Yards",
        barmode='group'
    )

    fig.show()

def plot_game_prediction(team1, team2, score1, score2, prob1, prob2):
    """Visualize win probabilities for a matchup using a pie chart."""
    fig = go.Figure(data=[
        go.Pie(
            labels=[team1, team2],
            values=[prob1, prob2],
            hoverinfo='label+percent',
            textinfo='label+percent',
            marker=dict(line=dict(color='#000000', width=2))
        )
    ])

    fig.update_layout(
        title=f"{team1} vs {team2} - Predicted Score: {score1} to {score2}",
    )

    fig.show()

def plot_predicted_yardage(team1, team2, off1, def1, off2, def2):
    categories = [team1, team2]
    fig = go.Figure()
    fig.add_trace(
        go.Bar(x=categories, y=[off1, off2], name="Predicted Offensive Yards")
    )
    fig.add_trace(
        go.Bar(x=categories, y=[def1, def2], name="Predicted Defensive Yards Allowed")
    )
    fig.update_layout(
        title=f"{team1} vs {team2} - Predicted Yardage",
        xaxis_title="Team",
        yaxis_title="Yards",
        barmode="group",
    )
    fig.show()

def plot_player_comparison(player_stats, stat_type="passingYards", top_n=5):
    filtered_players = [p for p in player_stats if p.get("statType") == stat_type]
    print(f"Found {len(filtered_players)} players with stat type: {stat_type}")

    if not filtered_players:
        print("No data to display for this stat type.")
        return

    sorted_players = sorted(filtered_players, key=lambda p: float(p.get("stat", 0) or 0), reverse=True)[:top_n]
    names = [p.get("player", "Unknown") for p in sorted_players]
    stats = [float(p.get("stat", 0)) for p in sorted_players]

    print(f"Players: {names}")
    print(f"Stats: {stats}")

    fig = go.Figure([go.Bar(x=names, y=stats)])
    fig.update_layout(
        title=f"Top {top_n} Players by {stat_type}",
        xaxis_title="Player",
        yaxis_title=stat_type,
        template="plotly_white"
    )
    fig.show()

def plot_team_roster(team, roster):
    if not roster:
        print("No roster data available.")
        return

    names = [p.get("lastName", "Unknown") for p in roster]
    positions = [p.get("position", "") for p in roster]
    jerseys = [p.get("jersey", "") for p in roster]

    table = go.Table(
        header=dict(values=["Last Name", "Position", "Jersey"], fill_color="paleturquoise", align="left"),
        cells=dict(values=[names, positions, jerseys], fill_color="lavender", align="left"),
    )
    fig = go.Figure(data=[table])
    fig.update_layout(title=f"{team} Roster")
    fig.show()

