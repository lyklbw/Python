import csv
from matplotlib import pyplot as plt

filename = 'KalmanPredict.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = row[2]
        high = float(row[0])
        low = float(row[1])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)

plt.title("Kalman Filter Predictions", fontsize=24)
plt.xlabel('', fontsize=16)

plt.ylabel("position", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()