## College Football Matchup Analyzer

This tool compares two FBS teams' season stats using data from the [CollegeFootballData API](https://collegefootballdata.com/), predicts a score based on offensive/defensive yardage, and visualizes a stat comparison using Plotly.

### Features

* Retrieves live team stats from the CollegeFootballData API
* Predicts scores based on total offensive and defensive yards
* Forecasts each team's offensive yards and defensive yards allowed
* Visualizes side-by-side stat comparisons using Plotly
* Displays predicted scores with win probabilities in a Plotly pie chart
* Displays stat summaries (total yards, offense and defense) in Plotly bar charts
* Command-line interface for interactive use
* Includes automated tests using Pytest

---

### How It Works

1. You input two FBS teams and a season year.
2. The app fetches season-long team stats from the API.
3. It calculates predicted scores using total yards gained and allowed.
4. Bar charts visualize stat comparisons and predicted scores with win probabilities using Plotly.

---

### Setup Instructions

#### 1. Clone the repo

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

#### 2. Create and activate your virtual environment

```bash
conda create -n matchup-env python=3.11
conda activate matchup-env
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

#### 4. Add your API key

Create a `.env` file in the root directory (same level as `main.py`) and add:

```
CFB_API_KEY=your_actual_api_key_here
```

*Don’t commit this file to GitHub. Keep it secret!*

#### 5. Run the app

```bash
python main.py
```

#### 6. Run the tests

```bash
pytest
```

---

### File Structure

```
.
├── data_fetcher.py     # API call logic
├── utils.py            # Stat extraction + score prediction
├── matchup.py          # Core logic to simulate a game
├── visuals.py          # Plotly-based graphing
├── main.py             # Entry point for running the app
├── test_matchup.py     # Pytest tests
├── .env                # Your local API key (not tracked)
├── requirements.txt    # All dependencies
└── README.md           # This file
```

---

### License

MIT License. See [LICENSE](./LICENSE) for details.

---

### Security Notes

* API keys are stored in `.env` and loaded with `python-dotenv`.
* `.env` is included in `.gitignore` to prevent accidental exposure.



