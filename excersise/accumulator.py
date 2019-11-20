'''Write a program which take read 10 files in a folder and using accumulator
Calaculate the total number of line in each file'''

from pyspark import SparkContext
import re

sc = SparkContext("local", "ForEach app")
total = sc.accumulator(0)
recordsRDD = sc.textFile("in/*")

def filereader(records):
    total.add(1)

totalRecordsRdd=recordsRDD.map(filereader)
print(totalRecordsRdd.count())
print("Total lines in each file: {}".format(total.value))

