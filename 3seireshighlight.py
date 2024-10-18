import matplotlib
matplotlib.use('TkAgg')  # You can also try 'Qt5Agg' or 'Agg'

import matplotlib.pyplot as plt  #
import numpy as np
import mplcursors
from mpl_toolkits.mplot3d import Axes3D



#points per game
x = [43.2, 25.8, 43.5, 35.2, 36.8, 35.7, 32.6, 26.8, 34.2, 20.5, 33, 41.6, 20.8, 26.8, 30, 44.2, 21.2, 22.8, 29.4, 24.3, 22.3, 26.4, 30.6, 29.6, 27.5, 26.4, 22.4, 36.6, 29.4, 13.7, 21.4, 46, 41.7, 30.7, 27, 25.6, 39, 19.8, 30.6, 34.2, 17.7, 23.5, 25.4, 32.2, 30.5, 18.8, 22, 25.6, 22.4, 26.2, 31, 40, 26.2, 20.8, 28.5, 29.4, 30.4, 28.2, 21.4, 24.6, 25.8, 34.4, 20.4, 15.8, 27.8, 24.2, 14.8, 37.2, 21.6, 24, 40.6, 20.4, 32.2, 19.6, 25.4, 24.6, 23, 25.4, 30.6, 24.6, 26.4, 14.5, 28.2, 27.8, 27.4, 36.8, 45, 23.2, 23.7, 23.2, 26.4, 32.8, 29, 21.6, 31.8, 21.8, 23.8, 27.8, 28.6, 28.2, 29.4, 26.6, 20.8, 19.8, 23.6, 32.8, 29.6, 25.2, 28.6, 22.8, 23.8, 19.2, 21.6, 20.6, 22.8, 25, 22.6, 28.8, 22.8, 24.2, 26.4, 29.6, 21.4, 26.2, 16.6, 21.6, 21.6, 24.8, 22.8, 22.8, 18.6, 20.6, 22.8, 23.8] 

#points allowed
y = [6.3, 27.4, 11, 11.7, 12.2, 12.3, 12.6, 13, 14.5, 14.5, 17, 17.2, 17.6, 18, 18.4, 18.4, 18.5, 18.8, 19, 19, 19.3, 19.5, 20, 20.2, 20.3, 20.4, 20.4, 20.4, 38.2, 20.5, 20.6, 20.8, 20.8, 20.8, 21.2, 21.2, 21.4, 21.4, 21.4, 21.7, 22, 22.3, 22.3, 22.6, 22.7, 45.4, 22.8, 23, 23, 23.2, 23.6, 23.8, 23.8, 24.6, 23.8, 24, 24, 24, 24.4, 24.6, 25, 24.8, 25, 22.3, 25.2, 25.6, 25.3, 25.4, 25.4, 25.6, 26.2, 26.4, 26.8, 27.6, 27, 27.6, 27.7, 27.8, 28.2, 28.2, 28.4, 28.5, 28.6, 28.6, 28.6, 28.6, 28.6, 28.8, 29, 29, 29.8, 29.8, 30, 30, 30, 30, 30.8, 30.8, 31, 31, 31, 31, 31, 31.6, 32, 32, 32.2, 32.6, 33, 33, 33, 33, 34.8, 35.2, 35.6, 35.8, 36.6, 37.4, 37.8, 38, 38, 38.4, 38.6, 38.6, 39, 40, 40.6, 41, 41.2, 41.8, 42, 42, 43.6, 44] 


#strength * 100 and negatives turned
z = [8.8, -4.8, 11.2, 8.3, 9.1, 9, 5.6, -3.1, 6.7, 8.4, 4.7, -1.8, -5.8, 10.1, 2.4, -6.6, 3.1, 4.1, -3.5, 12.1, 1.5, -6.1, 15.1, 2.2, 11.2, -3.8, 1, 9.1, -8.4, 6.4, 1, 5.8, 12.5, 10.8, 8.6, -8, -7, 0.1, 4.6, 7, -1.4, 7.1, -8.2, 9.7, 4.7, -7.7, 0.7, 8, 2.7, -4.8, 7.7, -0.8, -1.1, -10.2, 1.8, 7.2, 2.8, 0.6, 5.6, -3.6, -5.7, 0.6, -5.4, 3, -0.3, -8.6, 7.5, 5.2, -4.3, -6.2, 3.4, -4.8, -1.7, -3.4, -6.4, 9.8, -3.2, 2.4, 6.3, 3.2, 7.4, 8.3, -2.2, -6.9, 3, 1.3, 1.3, -5.6, -6.2, -6.7, 2.7, -0.1, -3.6, 0.5, -0.7, -4.5, -9.1, -1.2, -3.7, -2.3, -2.7, -4.2, -5.6, -4.5, -2.5, -6.6, -7.6, -5.1, 3.1, -3.2, -2.4, -4.7, -1.2, -7.2, -1.5, -7.3, -4.7, -6.2, -7.4, 8, 4.6, 9.4, -2.4, -8.2, -6.5, -7.5, -8.5, -7.8, -9, -9.2, 1.5, -6.8, -7.3, -7.6] #str


# Define colors and sizes for the points

#team names
labels = ["Texas", "Army", "Ohio St", "Notre Dame", "Tennessee", "Mississippi", "Iowa St", "Nebraska", "Penn St", "Kentucky", "BYU", "Indiana", "N Illinois", "Texas A&M", "Missouri", "James Madison", "Minnesota", "California", "Memphis", "Oklahoma", "Washington", "Navy", "Georgia", "Cincinnati", "S Carolina", "Duke", "Utah", "Oregon", "Liberty", "Houston", "Boston Col", "Miami", "Alabama", "USC", "Iowa", "UL Monroe", "Texas St", "Northwestern", "Wisconsin", "Clemson", "Miami (OH)", "Michigan", "Connecticut", "LSU", "VA Tech", "LA Tech", "Rutgers", "Arkansas", "Arizona St", "Toledo", "Louisville", "UNLV", "Virginia", "Sam Hous St", "GA Tech", "Kansas St", "Colorado", "Illinois", "Auburn", "San Diego St", "Buffalo", "Pittsburgh", "Louisiana", "Michigan St", "Maryland", "Florida Intl", "Florida St", "S Methodist", "Bowling Green", "Hawaii", "Tulane", "San Jose St", "Syracuse", "Ohio", "Fresno St", "Florida", "Old Dominion", "UCF", "Vanderbilt", "Baylor", "W Virginia", "UCLA", "Oregon St", "W Kentucky", "Oklahoma St", "Texas Tech", "Boise St", "E Carolina", "Nevada", "E Michigan", "Arizona", "Wash State", "Fla Atlantic", "Kansas", "Rice", "S Alabama", "Jksnville St", "Troy", "Georgia St", "Colorado St", "Marshall", "Arkansas St", "Charlotte", "Central Mich", "Air Force", "Coastal Car", "U Mass", "GA Southern", "N Carolina", "NC State", "Wyoming", "W Michigan", "Stanford", "North Texas", "UTSA", "TX El Paso", "Temple", "S Florida", "S Mississippi", "TX Christian", "Wake Forest", "Miss State", "Tulsa", "Kennesaw St", "Akron", "N Mex State", "Middle Tenn", "App State", "New Mexico", "UAB", "Purdue", "Ball St", "Utah St", "Kent St"
]  # Labels for each point
top_25_teams = ["Georgia", "Michigan", "Ohio St", "Florida St", "Washington", "Oregon", "Texas", "Alabama", "Penn St", "USC", "Notre Dame", "Oklahoma", "Tennessee", "Mississippi", "LSU", "North Carolina", "Duke", "Utah", "Oregon St", "UCLA", "Missouri", "Kansas", "Kansas St", "Tulane", "Louisville"]

colors = np.array([ 'red' if label in top_25_teams else 'blue' for label in labels])
sizes = [(s + 11) * 5 for s in z]  # Scale sizes based on strength of schedule


fig, ax = plt.subplots()

# Scatter plot with x (Points Per Game), y (Points Allowed), and z (size of points)
scatter = ax.scatter(x, y, c=colors, s=sizes, alpha=0.8)

# Add axis labels
ax.set_xlabel('Points Per Game')
ax.set_ylabel('Points Allowed')

# Add title
ax.set_title('FBS Week 7 Stats - Top 25 Teams Highlighted in Red')

# mplcursors to show labels on click
cursor = mplcursors.cursor(scatter)

@cursor.connect("add")
def on_add(sel):
    # Customize the text shown when a point is clicked
    sel.annotation.set_text(f"{labels[sel.index]}\nPoints Per Game: {x[sel.index]}\nPoints Allowed: {y[sel.index]}\nStrength of Schedule: {z[sel.index]}")

# Function to highlight a specific team
def highlight_team(team_name):
    if team_name in labels:
        index = labels.index(team_name)
        ax.scatter(x[index], y[index], c='green', s=sizes[index] * 2, edgecolor='black', linewidth=2)  # Highlight team in green
        ax.annotate(f"{team_name}", (x[index], y[index]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=12, fontweight='bold', color='green')
        plt.draw()
    else:
        print(f"Team '{team_name}' not found in the data.")

# Example usage: highlight_team('Georgia')  # You can search for a team by calling this function

# Show the plot
plt.show()

highlight_team("Texas")
# You can now run highlight_team('TeamName') to highlight individual teams