import csv
import numpy as np

def gettingSomething(data_path):
	marks = []
	days = []
	with open(data_path) as path:
		reader = csv.DictReader(path)
		for row in reader:
			marks.append(float(row["Marks In Percentage"]))
			days.append(float(row["Days Present"]))
	return{"x" : marks, "y" : days}


def findCorrelation(source):
    correlation = np.corrcoef(source["x"], source["y"])
    print("Correlation Between Marks Percentage And Days Present is ",correlation[0,1])

def setup():
    data_path  = "./Student Marks vs Days Present.csv"

    source = gettingSomething(data_path)
    findCorrelation(source)

setup()