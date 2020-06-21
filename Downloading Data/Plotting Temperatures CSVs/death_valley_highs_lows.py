import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader) # Stores items in a list
	
	# Grab index associated with columns
	#for index, column_header in enumerate(header_row):
		#print(index, column_header)
		
	# Get dates and high temperatures from this file.
	dates, highs, lows = [], [], []
	for row in reader: # Returns each line following it's position from the previous next function
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			high = int(row[4])
			low = int(row[5])
		except ValueError:
			print(f"Missing data for {current_date}")
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)
		
# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5) # Plot points and connect with line
ax.plot(dates, lows, c='blue', alpha=0.5) # Alpha controls color transparency 0 is completely transparent and 1 is completely opaque
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) # Fills space between two y-value series and takes a series of x-values and two y-values
# Facecolor determines the color of the shaded region

# Format plot.
title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate() # fig.autofmt_xdate() draws the date labels diagonally to prevent them from overlapping
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()