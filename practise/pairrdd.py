from pyspark import SparkConf,SparkContext 
import re
class Utils():
    COMMA_DELIMITER = re.compile(''',(?=(?:[^"]*"[^"]*")*[^"]*$)''')

if __name__ == "__main__":
    conf = SparkConf().setAppName("pairrdd").setMaster("local[*]")
    sc = SparkContext(conf = conf)

    txtfile=sc.textFile("airports.text")
    newtxtfile=txtfile.map(lambda line:(Utils.COMMA_DELIMITER.split(line)[1],Utils.COMMA_DELIMITER.split(line)[3]))

    # print(newtxtfile.take(10))

    airportnotinusa=newtxtfile.filter(lambda keyvalue:keyvalue[1]!="\"Greenland\"")

    print(airportnotinusa.take(10))
