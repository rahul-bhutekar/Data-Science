import pandas as pd
import numpy as np
import streamlit as st

# Enable wide mode
st.set_page_config(layout="wide")

st.title(':trophy: IPL EDA - Streamlit app:cricket_bat_and_ball:')
st.divider()

st.markdown('#### :red[:hash: read file using *read_csv* function: ] :orange[pd.read_csv(), head(), tail()] ')
df_ball_to_ball = pd.read_csv('https://raw.githubusercontent.com/rahul-bhutekar/Data-Science/main/Assignments/EDA/EDA_IPL/dataset/IPL%20Ball-by-Ball%202008-2020.csv')

df_match = pd.read_csv('https://raw.githubusercontent.com/rahul-bhutekar/Data-Science/main/Assignments/EDA/EDA_IPL/dataset/IPL%20Matches%202008-2020.csv')

st.write('Ball-by-Ball dataset :orange[head()]')
st.table(df_ball_to_ball.tail())
st.write('IPL Matches dataset :orange[tail()]')
st.table(df_match.tail())

st.markdown('#### :red[:hash: number of rows and columns: ] :orange[df.shape] ')
st.write('Ball-by-Ball :orange[shape]')
st.write(df_ball_to_ball.shape)
st.write('IPL Matches :orange[shape]')
st.write(df_match.shape)

st.markdown('#### :red[:hash: data type of each column: ] :orange[df.dtypes] ')
st.write('Ball-by-Ball :orange[dtypes]')
st.table(df_ball_to_ball.dtypes)
st.write('IPL Matches :orange[dtypes]')
st.table(df_match.dtypes)

st.markdown('#### :red[:hash: summary of the data: *column names, total no.of non-null values, data types, memory usage*: ] :orange[df.info()] ')
st.write('Ball-by-Ball :orange[info()]')
st.write(df_ball_to_ball.info())
st.write('IPL Matches :orange[info()]')
st.write(df_match.info())

st.markdown('#### :red[:hash: summary statistics for numeric data types: ] :orange[df.describe()] ')
st.write('Ball-by-Ball :orange[describe()]')
st.write(df_ball_to_ball.describe())
st.write('Ball-by-Ball :orange[describe(include="O")] for "objects" datatype ')
st.write(df_ball_to_ball.describe(include='O'))
st.write('IPL Matches :orange[describe(include="all")]')
st.write(df_match.describe(include='all'))

st.markdown('#### :red[:hash: count of missing values: ] :orange[df.isna()] ')
st.write('Ball-by-Ball :orange[isna()]')
st.table(df_ball_to_ball.isna().sum())
st.write('IPL Matches :orange[isna()]')
st.table(df_match.isna().sum())

df_ball_to_ball['dismissal_kind'] = df_ball_to_ball['dismissal_kind'].fillna('no_dismissal')
df_ball_to_ball['player_dismissed'] = df_ball_to_ball['player_dismissed'].fillna('no_player_dismissed')
df_ball_to_ball['fielder'] = df_ball_to_ball['fielder'].fillna('no_fielder')
df_ball_to_ball['extras_type'] = df_ball_to_ball['extras_type'].fillna('no_extras')
df_ball_to_ball['bowling_team'] = df_ball_to_ball['bowling_team'].fillna('no_bowling_team')

df_match['player_of_match'] = df_match['player_of_match'].fillna('no_player_of_match')
df_match['result_margin'] = df_match['result_margin'].fillna('0.0')
df_match['eliminator'] = df_match['eliminator'].fillna('no_eliminator')
df_match['method'] = df_match['player_of_match'].fillna('no_method')
df_match['winner'] = df_match['winner'].fillna('no_winner')
df_match['result'] = df_match['result'].fillna('no_result')

st.markdown('#### :red[:hash: count of duplicate rows: ] :orange[df.duplicated()] ')
st.write('Ball-by-Ball :orange[duplicated()]')
st.write(df_ball_to_ball[df_ball_to_ball.duplicated()].shape)
st.write('IPL Matches :orange[duplicated()]')
st.write(df_match[df_match.duplicated()].shape)

df_match['team1'] = df_match['team1'].replace('Rising Pune Supergiant','Rising Pune Supergiants')
df_match['team2'] = df_match['team2'].replace('Rising Pune Supergiant','Rising Pune Supergiants')

df_match['city'] = np.where(df_match['venue'] == 'Dubai International Cricket Stadium', 'Dubai', df_match['city'])
df_match['city'] = np.where(df_match['venue'] == 'Sharjah Cricket Stadium', 'Sharjah', df_match['city'])

st.subheader('Q1. What was the count of matches played in each season?', divider='rainbow')
match_dates = pd.to_datetime(df_match['date'])
match_years = match_dates.dt.year 
    # .dt: This is the accessor that allows you to access datetime properties and methods.
    # .year: This is a datetime property that extracts the year component from each datetime object in the Series.
count_of_matches = match_years.value_counts().sort_index()
st.table(count_of_matches)

st.subheader('Q2. How many runs were scored in each season?', divider='rainbow')
df_match['year'] = match_years
df_merge = pd.merge(df_ball_to_ball, df_match[['id', 'year']], on='id', how='inner')
    # on='id': This specifies the column(s) on which to join the DataFrames. In this case, we specify 'id' as the common column between the two DataFrames.
    # how='inner': This specifies the type of join to perform. 'inner' means that only the rows with matching 'id' values in both DataFrames will be included in the result.

total_runs_per_season = df_merge.groupby('year')['total_runs'].sum()
st.table(total_runs_per_season)

st.subheader('Q3. What were the runs scored per match in different seasons?', divider='rainbow')
runs_scored_per_match = df_ball_to_ball.groupby('id')['total_runs'].sum()
st.table(runs_scored_per_match.head(10))

st.subheader('Q4. Who has umpired the most?', divider='rainbow')
umpire_list = pd.concat([df_match['umpire1'], df_match['umpire2']])
umpire_count = umpire_list.value_counts()
name = umpire_count.idxmax() # returns the index (umpire's name) corresponding to the maximum count
count = umpire_count.max()
st.write(f"'{name}' has umpired the most with with {count} matches.")

st.subheader('Q5. Which team has won the most tosses?', divider='rainbow')
count_teams_won_toss = df_match['toss_winner'].value_counts()
st.write(f"'{count_teams_won_toss.idxmax()}' with {count_teams_won_toss.max()} toss wins.")

st.subheader('Q6. What does the team decide after winning the toss?', divider='rainbow')
team_with_most_toss_wins_with_decision = df_match[df_match['toss_winner'] == count_teams_won_toss.idxmax()]['toss_decision']
decision_taken = team_with_most_toss_wins_with_decision.value_counts()
st.write(f"The '{count_teams_won_toss.idxmax()}' decided to {decision_taken.idxmax()}({decision_taken.max()}) first after winning the toss.")

st.subheader('Q7. How does the toss decision vary across seasons?', divider='rainbow')
toss_decision_counts = df_match.groupby(['year', 'toss_decision']).size()
toss_decision_counts = toss_decision_counts.reset_index(name='count')
toss_decision_counts_pivot = toss_decision_counts.pivot(index='year', columns='toss_decision', values='count')
st.table(toss_decision_counts_pivot)


st.subheader('Q8. Does winning the toss imply winning the game?', divider='rainbow')
total_matches = df_match.shape[0]

matches_won_with_toss_win = df_match[df_match['toss_winner'] == df_match['winner']]

percentage_wins_with_toss_win = ( matches_won_with_toss_win.shape[0] / total_matches ) * 100
st.write(f"Percentage of matches won by the team that won toss: {percentage_wins_with_toss_win:.2f}%") 

st.subheader('Q9. How many times has the chasing team won the match?', divider='rainbow')
matches_won_by_chasing_team = total_matches - matches_won_with_toss_win.shape[0]
st.write(f'The chasing team has won {matches_won_by_chasing_team} times out of {total_matches} matches.')

st.subheader('Q10. Which all teams had won this tournament?', divider='rainbow')
seasons = match_years.unique()
last_match_winner_per_season = df_match.groupby('year')['winner'].last()
st.table(last_match_winner_per_season)

st.subheader('Q11. Which team has played the most number of matches?', divider='rainbow')
matches_played_by_teams_list = pd.concat([df_match['team1'], df_match['team2']])
matches_played_by_teams_count = matches_played_by_teams_list.value_counts()

st.write(f"'{matches_played_by_teams_count.idxmax()}' has played the most number of matches {matches_played_by_teams_count.max()}")

st.subheader('Q12. Which team has won the most number of times?', divider='rainbow')
team_with_win_counts = df_match['winner'].value_counts()
st.write(f"'{team_with_win_counts.idxmax()}' has won the most number of times- {team_with_win_counts.max()} times.")


st.subheader('Q13. Which team has the highest winning percentage?', divider='rainbow')
total_matches_per_team = df_match['team1'].value_counts() + df_match['team2'].value_counts()

number_of_matches_won_per_team = df_match['winner'].value_counts()

percentage_wins_per_team = (number_of_matches_won_per_team/total_matches_per_team) * 100
st.write(f"The team '{percentage_wins_per_team.idxmax()}' has the highest winning percentage- {percentage_wins_per_team.max():.2f}%")

st.subheader('Q14. Is there any lucky venue for a particular team?', divider='rainbow')
teams_lists = pd.concat([df_match['team1'], df_match['team2']])
teams = teams_lists.unique()

for team in teams:
    team_matches = df_match[(df_match['team1'] == team) | (df_match['team2'] == team)]
    matches_per_venue = team_matches['venue'].value_counts()
    most_played_venues = matches_per_venue[:5]
    matches_won_per_venue = team_matches[team_matches['winner'] == team]['venue'].value_counts()
    winning_percentage = ( matches_won_per_venue / most_played_venues ) * 100
    st.write(f"For team '{team}' the venue '{winning_percentage.idxmax()}' is luckiest with {winning_percentage.max():.2f}% of win")

st.subheader('Q15. Innings wise comparison between teams', divider='rainbow')
innings_per_match_per_season_summary = df_merge.groupby(['id', 'batting_team', 'year'])[['batsman_runs', 'extra_runs', 'total_runs', 'is_wicket']].sum()
st.table(innings_per_match_per_season_summary.head(5))


st.subheader('Q16. Which team has scored the most number of 200+ scores?', divider='rainbow')
runs_per_match_id = df_ball_to_ball.groupby(['id', 'batting_team'])['total_runs'].sum().reset_index()
high_score_inning = runs_per_match_id[runs_per_match_id['total_runs'] >= 200]
team_highscore_count = high_score_inning['batting_team'].value_counts()

st.write(f"The team '{team_highscore_count.idxmax()}' has scored most amount of 200+ runs- {team_highscore_count.max()} times")


st.subheader('Q17. Which team has conceded 200+ scores the most?', divider='rainbow')
runs_per_match_id_bowling = df_ball_to_ball.groupby(['id', 'bowling_team'])['total_runs'].sum().reset_index()
high_score_conceded_inning = runs_per_match_id_bowling[runs_per_match_id_bowling['total_runs'] >= 200]
team_highscore_conceded_count = high_score_conceded_inning['bowling_team'].value_counts()
st.write(f"The team '{team_highscore_conceded_count.idxmax()}' has conceded most amount of 200+ runs- {team_highscore_conceded_count.max()} times")

st.subheader('Q18. What was the highest run scored by a team in a single match?', divider='rainbow')
st.write(runs_per_match_id.max())

st.subheader('Q19. Which is the biggest win in terms of run margin?', divider='rainbow')
biggest_run_margin = df_match[df_match['result'] == 'runs']['result_margin'].max()
st.write(biggest_run_margin)

st.subheader('Q20. Which batsmen have played the most number of balls?', divider='rainbow')
balls_faced_by_batsman = df_ball_to_ball['batsman'].value_counts()
st.write(f"'{balls_faced_by_batsman.idxmax()}' has played the most number of balls- {balls_faced_by_batsman.max()} balls.")

st.subheader('Q21. Who are the leading run-scorers of all time?', divider='rainbow')
runs_scored_by_batsman = df_ball_to_ball.groupby('batsman')['batsman_runs'].sum()
st.write(f"\'{runs_scored_by_batsman.idxmax()}\' is the leading run-scorers of all time with {runs_scored_by_batsman.max()} runs.")

st.subheader('Q22. Who has hit the most number of 4\'s?', divider='rainbow')
batsman_with_most_fours = df_ball_to_ball[df_ball_to_ball['total_runs'] == 4]['batsman'].value_counts()
st.write(batsman_with_most_fours[:5])

st.subheader('Q23. Who has hit the most number of 6\'s?', divider='rainbow')
batsman_with_most_sixes = df_ball_to_ball[df_ball_to_ball['total_runs'] == 6]['batsman'].value_counts()
st.write(batsman_with_most_sixes[:5])

st.subheader('Q24. Who has the highest strike rate?', divider='rainbow')
strike_rate = ( runs_scored_by_batsman / balls_faced_by_batsman ) * 100
st.write(f"'{strike_rate.idxmax()}' has the highest strike rate- {strike_rate.max():.2f}")

st.subheader('Q25. Who is the leading wicket-taker?', divider='rainbow')
leading_wicket_taker = df_ball_to_ball[df_ball_to_ball['is_wicket'] == 1]['bowler'].value_counts()
st.write(f"'{leading_wicket_taker.idxmax()}' is the leading wicket taker with {leading_wicket_taker.max()} wickets")

st.subheader('Q26. Which stadium has hosted the most number of matches?', divider='rainbow')
matches_hosted_by_venues = df_match['venue'].value_counts()
st.write(f"'{matches_hosted_by_venues.idxmax()}' has hosted most of the matches- {matches_hosted_by_venues.max()}")

st.subheader('Q27. Who has won the most MOM awards?', divider='rainbow')
MOM_count = df_match['player_of_match'].value_counts()
st.write(f"'{MOM_count.idxmax()}' has won the most MOM awards- {MOM_count.max()} times")

st.subheader('Q28. What is the count of fours hit in each season?', divider='rainbow')
df_merge[df_merge['batsman_runs'] == 4]['year'].value_counts().sort_index()

st.subheader('Q29. What is the count of sixes hit in each season?', divider='rainbow')
number_of_six_per_season = df_merge[df_merge['batsman_runs'] == 6]['year'].value_counts().sort_index()
st.table(number_of_six_per_season)

st.subheader('Q30. What is the count of runs scored from boundaries in each season?', divider='rainbow')
number_of_four_per_season = df_merge[df_merge['batsman_runs'] == 4]['year'].value_counts().sort_index()
for value, count in number_of_four_per_season.items():
    st.write(f"count of runs scored from boundaries in {value} season: {count*4}")


st.subheader('Q31. What is the run contribution from boundaries in each season?', divider='rainbow')
total_runs_scored_per_season = df_merge.groupby('year')['total_runs'].sum()

for value, count in number_of_four_per_season.items():
    total_runs = total_runs_scored_per_season[value]
    percentage_runs_from_four = (count*4/total_runs)*100
    st.write(f"run contribution from boundaries in {value} season is: {percentage_runs_from_four:.2f}%")

st.subheader('Q32. Which team has scored the most runs in the first 6 overs?', divider='rainbow')
teams_score_in_first_six_overs = df_ball_to_ball[df_ball_to_ball['over'] <= 6].groupby('batting_team')['total_runs'].sum()
st.write(f"The team who scored the most runs in the first 6 overs is '{teams_score_in_first_six_overs.idxmax()}' with {teams_score_in_first_six_overs.max()} runs.")

st.subheader('Q33. Which team has scored the most runs in the last 4 overs?', divider='rainbow')
teams_score_in_last_four_overs = df_ball_to_ball[df_ball_to_ball['over'] >= 16].groupby('batting_team')['total_runs'].sum()
st.write(f"The team who scored the most runs in the last 4 overs is '{teams_score_in_last_four_overs.idxmax()}' with {teams_score_in_last_four_overs.max()} runs.")

st.subheader('Q34. Which team has the best scoring run-rate in the first 6 overs?', divider='rainbow')
teams_with_run_rate_for_first_six_overs = teams_score_in_first_six_overs/36
st.write(f"The team who has the best scoring run-rate in the first 6 overs is \'{teams_with_run_rate_for_first_six_overs.idxmax()}\' with {teams_with_run_rate_for_first_six_overs.max()} run-rate.")

st.subheader('Q35. Which team has the best scoring run-rate in the last 4 overs?', divider='rainbow')
teams_with_run_rate_for_last_four_overs = teams_score_in_last_four_overs/24
st.write(f"The team who has the best scoring run-rate in the last 4 overs is '{teams_with_run_rate_for_last_four_overs.idxmax()}' with {teams_with_run_rate_for_last_four_overs.max():.2f} run-rate.")

st.markdown('# Graphs - Visualization :bar_chart: ')
import plotly.express as px
import plotly.graph_objects as go

fig = px.bar(count_of_matches, y=count_of_matches.values, x=count_of_matches.index, text_auto='.2s',
            title="Bar Graph - Matches per season",
            color=count_of_matches.index)

fig.update_layout(
    xaxis_title="Season", 
    yaxis_title="Number of Matches",
    height=450, width=1000
)

fig

top_10_leading_run_scorers = runs_scored_by_batsman.sort_values(ascending=False)[:10]
colors = ['rgb(221,21,21)','rgb(219,138,29)','rgb(209,219,29)','rgb(240,240,240)', 'rgb(29,219,45)','rgb(29,219,193)','rgb(29,126,219)','rgb(100,29,219)','rgb(163,29,219)','rgb(221,21,65)']
fig = go.Figure(go.Bar(
            x=top_10_leading_run_scorers.values,
            y=top_10_leading_run_scorers.index,
            orientation='h',
            marker_color=colors))

fig.update_layout(
    xaxis_title="Runs scored",  
    yaxis_title="Player Name", 
    title="Top 10 leading run scorers",
    height=350, width=1000
)

fig

top_10_leading_wicket_taker = leading_wicket_taker.sort_values(ascending=False)[:10]
fig = px.bar(top_10_leading_wicket_taker, 
             x=top_10_leading_wicket_taker.values, 
             y=top_10_leading_wicket_taker.index, orientation='h', 
             color=top_10_leading_wicket_taker.index)

fig.update_layout(
    xaxis_title="Number of Wickets",  
    yaxis_title="Player Name", 
    title="Top 10 leading wicket takers",
    height=400, width=1000
)

fig

data = [
    {'year': number_of_four_per_season.index[i],
     'four': number_of_four_per_season.values[i]*4,
     'six': number_of_six_per_season.values[i]*6,
     'total_runs': total_runs_per_season.values[i]}
    for i in range(len(number_of_four_per_season.index))
]
df = pd.DataFrame(data)

# Create a bar plot using Plotly Express
fig = px.bar(df, x='year', y=['four', 'six', 'total_runs'], 
             labels={'value': 'Runs', 'variable': 'Statistic'},
             title='Cricket Runs Statistics per Season')

fig.update_layout(height=500, width=1000) 

# Show the plot
fig

y = matches_played_by_teams_count.values
x= matches_played_by_teams_count.index

# Create a filled line trace
fig = go.Figure(data=go.Scatter(
                    x=x,
                    y=y,
                    fill='tozeroy',
                    fillcolor='rgb(64,100,206)'
                ))

fig.update_layout(
    title="Matches played by teams",
    xaxis_title="Team Name",
    yaxis_title="Matches",
    height=500, width=800
)

fig

total_runs_per_team_2008 = df_merge.groupby(['batting_team', 'year'])['total_runs'].sum().reset_index()
# st.write(total_runs_per_team_2008 )
fig = px.line(total_runs_per_team_2008, x=total_runs_per_team_2008['year'], y=total_runs_per_team_2008['total_runs'], color=total_runs_per_team_2008['batting_team'], 
              markers=True, title='Total runs scored by each team every season')

fig.update_layout(height=500, width=1300, xaxis_title="Year", yaxis_title="Total Runs") 

fig

import time
_TEXT = '''
Please click [here](https://github.com/rahul-bhutekar/Data-Science/tree/main/Assignments/Streamlit/EDA_IPL) to get the source code for this Streamlit application.
'''

def github_code():
    for word in _TEXT.split(" "):
        yield word + " "
        time.sleep(0.02)

if st.button("get code"):
    st.write_stream(github_code)

