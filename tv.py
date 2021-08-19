import csv
import numpy as np

def getDataSource(data_path):
    cups_of_coffe = []
    hours_of_sleep = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            cups_of_coffe.append(float(row["sleep in hours"]))
            hours_of_sleep.append(float(row["\t coffe in ml"]))

    return{"x": cups_of_coffe, "y":hours_of_sleep}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between sleep in hours and coffee in ml: \n ",correlation[0,1])

def setup():
    data_path = "Data/cups of coffee vs hours of sleep.csv"
    datasource = getDataSource(data_path)

    findCorrelation(datasource)

setup()