import numpy as np
from scipy.integrate import quad
import csv



def optimal_mean(n, point_list):
    summation = 0
    for point in point_list:
        summation += point
    mean = summation / n


def optimal_sd(n, mean_star, point_list):
    summation = 0
    for point in point_list:
        summation += (point - mean_star)**2
    sd = np.sqrt(summation / n)

def calculate_probability_of_dimension(mean_star, sd_star, lower_bound, upper_bound):
    pass

def learn_means_and_sds():
    for month in range(1, 13):
        




#Load turtle data from csv file
file = open("Datasets/leatherbackturtle.csv", 'r')
csv_file = csv.reader(file, delimiter=',')

#Transform to numpy array
csv_dataset = []
for line in csv_file:
    csv_dataset.append(line)

np_dataset = np.array(csv_dataset[1:], dtype="unicode")

print(csv_dataset[1:])


print(calculate_probability_of_dimension(1.0, 1.0, 0.2, 0.4))