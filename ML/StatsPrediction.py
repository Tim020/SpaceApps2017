import csv
import os
from os import listdir
from os.path import isfile, join

def do_prediction(filename):
    print("Generating prediction data for", filename, "...")

    # Load turtle data from csv file
    file = open("Datasets/" + filename + ".csv", 'r')
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

    file.close()
    file = open("Datasets/Sightings By Month/" + filename + ".csv", 'w')
    csv_write = csv.writer(file, delimiter=',')
    month_data = []

    for i in range(1, 13):
        count = 0
        frequency_data = {}
        points_data = []
        for line in csv_dataset:
            if line[2] != "" and i == int(line[2]):
                count += 1
                if line[0] + line[1] not in frequency_data:
                    frequency_data[line[0] + "," + line[1]] = 1
                else:
                    frequency_data[line[0] + "," + line[1]] = frequency_data[line[0] + "," + line[1]] + 1
            points_data.append([int(line[0]), int(line[1])])
        for key in frequency_data:
            frequency_data[key] = frequency_data[key] / count
            csv_write.writerow([i, key.split(",")[0], key.split(",")[1], frequency_data[key]])
        month_data.append(frequency_data)

if not os.path.exists("Datasets/Sightings By Month/"):
    os.mkdir("Datasets/Sightings By Month/")

datasets = [f for f in listdir("Datasets/") if isfile(join("Datasets/", f))]

for set in datasets:
    do_prediction(set.split(".")[0])