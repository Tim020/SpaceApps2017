import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.integrate import quad, dblquad
import csv


def get_monthly_data_set(data_set, month):
    monthly_data_set = []
    latitudes = []
    longitudes = []

    for point in data_set:
        if point[2].item() == float(month):
            monthly_data_set.append(point)

    for point in monthly_data_set:
        latitudes.append((point[0]))
        longitudes.append(point[1])

    return [latitudes, longitudes]


def calculate_optimal_mean(n, point_list):
    summation = 0
    for point in point_list:
        summation += point
    mean = summation / n
    return mean


def calculate_optimal_sd(n, mean_star, point_list):
    summation = 0
    for point in point_list:
        summation += (point - mean_star)**2
    sd = np.sqrt(summation / n)
    return sd


def learn_monthly_parameters(data_set):
    monthly_parameters = []
    for dimension_type in data_set:
        mu = calculate_optimal_mean(len(dimension_type), dimension_type)
        sigma = calculate_optimal_sd(len(dimension_type), mu, dimension_type)
        monthly_parameters.append((mu, sigma))
    return monthly_parameters


def calculate_probability_of_dimension(mean_star, sd_star, lower_bound, upper_bound):
    def norm_func(x):
        y = 1 / (sd_star * np.sqrt(2 * np.pi)) * np.exp(-(x - mean_star) ** 2 / (2 * sd_star ** 2))
        return y

    return quad(norm_func, lower_bound, upper_bound)


def calculate_lat_long_prob_given_date(mean_star_lat, sd_star_lat, mean_star_long, sd_star_long, lower_bound, upper_bound, lower_boundary, upper_boundary):
    def norm_product(lat, long):
        y = 1 / (2 * np.pi * sd_star_lat * sd_star_long) * np.exp(-0.5 * ((lat - mean_star_lat)**2 / sd_star_lat**2) + (long - mean_star_long)**2 / sd_star_long**2)
        return y

    return dblquad(norm_product, lower_bound, upper_bound, lower_boundary, upper_boundary)

#Load turtle data from csv file
file = open("Datasets/leatherbackturtle.csv", 'r')
csv_file = csv.reader(file, delimiter=',')

#Transform to numpy array
csv_dataset = []
for line in csv_file:
    for column in line:
        column.replace("'","").replace("\n","")
    if line[0] is not "" and line[1] is not "" and line[2] is not "":
        csv_dataset.append([float(line[0]), float(line[1]), float(line[2])])

np_dataset = np.asarray(csv_dataset, dtype="float")

monthly_data_sets = []
for month in range(1, 13):
    monthly_data_sets.append(get_monthly_data_set(np_dataset, month))

means_and_sds = []
for month in range(12):
    means_and_sds.append(learn_monthly_parameters(monthly_data_sets[month]))


for line in means_and_sds:
    print(line)
    print((line[0][1] + line[1][1])/2)

