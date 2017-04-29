import numpy as np
import csv

# Load turtle data from csv file
file = open("Datasets/leatherbackturtle.csv", 'r')
csv_file = csv.reader(file, delimiter=',')

# Transform to numpy array
first_run = True
csv_dataset = []
for line in csv_file:
    if not first_run:
        line[0] = line[0].split(".")[0]
        line[1] = line[1].split(".")[0]
        line[2] = line[2].split(".")[0]
        csv_dataset.append(line)
    else:
        first_run = False

print(csv_dataset)
count = 0

month_data = []

for i in range(1, 13):
    count = 0
    frequency_data = {}
    for line in csv_dataset:
        if line[2] != "" and i == int(line[2]):
            count += 1
            if line[0] + line[1] not in frequency_data:
                frequency_data[line[0] + "," + line[1]] = 1
            else:
                frequency_data[line[0] + "," + line[1]] = frequency_data[line[0] + "," + line[1]] + 1
    month_data.append(frequency_data)
    print("Total data points for month", i, ":", count)
    print(count)
    print(len(frequency_data))
    print(frequency_data)
