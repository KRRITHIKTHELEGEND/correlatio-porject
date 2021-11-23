import csv
import numpy as np

def gettingSomething(data_path):
	coffee = []
	sleep = []
	with open(data_path) as path:
		reader = csv.DictReader(path)
		for row in reader:
			coffee.append(float(row["Coffee in ml"]))
			sleep.append(float(row["sleep in hours"]))
	return{"x" : coffee, "y" : sleep}


def findCorrelation(source):
    correlation = np.corrcoef(source["x"], source["y"])
    print("Correlation Between Coffee And Hours Of Sleep is ",correlation[0,1])

def setup():
    data_path  = "./cups of coffee vs hours of sleep.csv"

    source = gettingSomething(data_path)
    findCorrelation(source)

setup()