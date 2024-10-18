import matplotlib
matplotlib.use('TkAgg')  # You can also try 'Qt5Agg' or 'Agg'

import matplotlib.pyplot as plt  #
import numpy as np
import mplcursors
from mpl_toolkits.mplot3d import Axes3D


#Revenue $ to Win Percentage

teams = [
'Texas',
'Ohio State',
'Tennessee',
'Mississippi',
'Iowa State',
'Nebraska',
'Penn State',
'Kentucky',
'Indiana',
'Texas A&M',
'Missouri',
'Minnesota',
'California',
'Oklahoma',
'Washington',
'Georgia',
'Cincinnati',
'South Carolina',
'Utah',
'Oregon',
'Houston',
'Miami',
'Alabama',
'Iowa',
'Wisconsin',
'Clemson',
'Michigan',
'LSU',
'Virginia Tech',
'Rutgers',
'Arkansas',
'Arizona State',
'Louisville',
'Virginia',
'Georgia Tech',
'Kansas State',
'Colorado',
'Illinois',
'Auburn',
'Buffalo',
'Michigan State',
'Maryland',
'Florida International',
'Florida State',
'Florida',
'UCF',
'West Virginia',
'UCLA',
'Oregon State',
'Oklahoma State',
'Texas Tech',
'Arizona',
'Washington State',
'Kansas',
'North Carolina',
'NC State',
'Mississippi State',
'Purdue']

revenue = [
239290648.00, 251615345.00, 154566935.00, 133557937.00, 111287492.00, 143423944.00, 181227448.00, 159079024.00, 166761471.00, 193139619.00, 141157028.00, 135198272.00, 118212179.00, 177320217.00, 145184864.00, 203048566.00, 83344028.00, 142210807.00, 115719266.00, 153510555.00, 78088086.00, 214365357.00, 214365357.00, 151483092.00, 150100977.00, 158283618.00, 210652287.00, 199309382.00, 113000052.00, 109601529.00, 152513755.00, 121079615.00, 146225965.00, 161916231.00, 106635094.00, 100822204.00, 94873830.00, 145735330.00, 174568442.00, 40192255.00, 172799513.00, 107526374.00, 41043885.00, 161141884.00, 190417139.00, 89228205.00, 105193311.00, 103061344.00, 83480015.00, 104404398.00, 110154695.00, 119809120.00, 84069212.00, 80597220.00, 117474477.00, 93218236.00, 125498643.00, 146730938.00]

wp = [0.774, 0.827, 0.726, 0.628, 0.493, 0.429, 0.678, 0.508, 0.429, 0.596, 0.651, 0.439, 0.436, 0.622, 0.741, 0.816, 0.417, 0.545, 0.662, 0.689, 0.373, 0.514, 0.842, 0.563, 0.573, 0.64, 0.81, 0.726, 0.458, 0.478, 0.452, 0.455, 0.617, 0.505, 0.411, 0.69, 0.366, 0.438, 0.566, 0.476, 0.44, 0.469, 0.469, 0.632, 0.609, 0.584, 0.467, 0.42, 0.522, 0.516, 0.563, 0.494, 0.509, 0.47, 0.543, 0.456, 0.53, 0.534]
wp_of_100 = np.array(wp) * 100


colors = np.random.rand(len(revenue), 3)



# Create scatter plot
fig, ax = plt.subplots(figsize=(14, 8))
scatter = ax.scatter(wp_of_100, revenue, c=colors, s=100, alpha=0.8)

# Labels and grid
plt.title('College Football Teams: Revenue Vs Win Percentage', fontsize=20)
plt.xlabel("Win Percentage (%)")
plt.ylabel("Revenue (In Hundred Million) ($)")

# Add horizontal and vertical lines (you may need to adjust these based on your data)
ax.axhline(y=np.median(revenue), color='blue', linestyle='--')  # Median revenue
ax.axvline(x=np.median(wp_of_100), color='red', linestyle='--')  # Median win percentage

ax.grid(True)

# Invert the y-axis
ax.invert_yaxis()

# Add team names as text labels
for i, team in enumerate(teams):
    plt.annotate(team, (wp_of_100[i], revenue[i]), fontsize=8, ha='right')

# mplcursors to show labels on click
cursor = mplcursors.cursor(scatter)

@cursor.connect("add")
def on_add(sel):
    # Customize the text shown when a point is clicked
    team_index = sel.index
    sel.annotation.set_text(f"{teams[team_index]}\nWin %: {wp[team_index]}\nRevenue: {revenue[team_index]:,.2f}")

# Show the plot
plt.show()