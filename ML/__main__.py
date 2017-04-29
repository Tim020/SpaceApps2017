import numpy as np
import csv
import sklearn

#Load turtle data from csv file
file = open("Datasets/leatherbackturtle.csv", 'r')
csv_file = csv.reader(file, delimiter=',')

#Transform to numpy array
csv_dataset = []
for line in csv_file:
    csv_dataset.append(line)

np_dataset = np.array(csv_dataset[1:], dtype="unicode")

print(np_dataset)

dates = open("dates.txt", 'w')

for date in np_dataset[:, 2:]:
    dates.writelines(date[0][3:5] + '\n')