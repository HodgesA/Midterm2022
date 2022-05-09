from nba_history import player_data
from nba_history import team_data

df = player_data.scrape_player_salaries(start_year = 2000,
	end_year = 2000,
	export = True,
	sleep_time = 2)
	print(df.head())
df1 = team_data.scrape_nba_team_records(start_year = 2000,
	end_year = 2000,
	export = True)
	print(df1.head())
df2 = player_data.scrape_player_total_stats(start_year = 2000,
	end_year = 2000,
	export = True,
	sleep_time = 2)
	print(df2.head())
#Objective = find top earning players, performing teams for the year 2000