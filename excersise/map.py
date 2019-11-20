from pyspark import SparkContext
sc = SparkContext("local", "map app")

person_names=sc.textFile("person.csv")
rows=person_names.map(lambda line:line.split(","))

for row in rows.take(rows.count()):
    print(row[2])