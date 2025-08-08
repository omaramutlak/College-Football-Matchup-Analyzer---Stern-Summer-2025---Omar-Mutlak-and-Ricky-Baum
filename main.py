from matchup import simulate_matchup

def main():
    print("Welcome to the College Football Matchup Analyzer!")
    team1 = input("Enter Team 1: ")
    team2 = input("Enter Team 2: ")
    year = input("Enter Season Year (e.g. 2023): ")

    result = simulate_matchup(team1, team2, year)
    print("\n--- Matchup Result ---")
    print(result)

if __name__ == "__main__":
    main()











