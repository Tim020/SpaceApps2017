import csv

file = open("Datasets/bottlenosedolphin.csv", 'r')
csv_file = csv.reader(file, delimiter=',')
file2 = open("Dates.txt", 'w')

first_run = True
for line in csv_file:
    if not first_run:
        file2.write(line[2].split(" ")[0][5:7]+"\n")
    else:
        first_run = False
file.close()
file2.close()