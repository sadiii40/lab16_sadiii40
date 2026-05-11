"""
Program: Lab16- Ohio Unemployment Rate Plotter
Author: Sadikshya
Purpose: Reads the OHUR.csv file with Ohio's monthly unemployment rate 
since 1976, and creates a time line plot using mathplotlib. The plot is 
saved as an image file.
Date: 2026-05-11
"""

import matplotlib.pyplot as plt 
import csv
from datetime import datetime

dates = []
unemployment_rates = []

with open("OHUR.csv", "r") as file:
    reader = csv.reader(file)

    for index, row in enumerate(reader):
        if index == 0:
            #header row
            for col_index, col_name in enumerate(row):
                print(f"Column {col_index}: {col_name}")
            continue
        
        try:
            date = datetime.strptime(row[0], "%Y-%m-%d")
            rate = float(row[1])
        except ValueError as e:
            print(f"Skipping row {index} due to error: {e}")
        else:
            dates.append(date)
            unemployment_rates.append(rate)

#plot
plt.figure(figsize=(12, 5))
plt.plot(dates, unemployment_rates, linewidth=1.2, color="steelblue")

plt.title("Ohio Unemployment (by Month): 1976 - 2022", fontsize=14)
plt.xlabel("Date")
plt.ylabel("Unemp Rate")

plt.tight_layout()
plt.savefig("ohio_employment.png")
plt.show()

print("Plot saved to ohio_unemployment.png")