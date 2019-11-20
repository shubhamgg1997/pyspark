'''It is the variable that are used for aggregating information
across the executors.
We can calculate how many records are corrupted or counts 
events taht occur during job excution for debugging 
purposes

It is used normally for write data across all worker nodes

'''
'''from pyspark import SparkContext
sc=SparkContext("local","accumulator app")
num=sc.accumulator(10)

def f(x):
    global num
    num+=x

rdd=sc.parallelize([20,30,40,50])
rdd.foreach(f)
final=num.value
print("Accumulated value is %i ->"%(final))'''

from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    conf = SparkConf().setAppName("accumlator").setMaster("local[*]")
    sc = SparkContext(conf = conf)

    txtfile=sc.textFile("")
