import csv
import numpy as np

def getDataSource(data_path):
    percentage = []
    days_present = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            percentage.append(float(row["marks in percentage"]))
            days_present.append(float(row["\t DAYS PRESENT"]))

    return{"x": percentage, "y":days_present}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between student marks vs days present: \n ",correlation[0,1])

def setup():
    data_path = "Data/Student Marks vs Days Present.csv"
    
    datasource = getDataSource(data_path)

    findCorrelation(datasource)

setup()