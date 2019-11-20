from pyspark import SparkContext
sc = SparkContext("local", "tranformationapp")
import functools as ft
import string 
from operator import add
#filter out even number
# l=list(range(1,10))
# lRDD=sc.parallelize(l)
# lEven=lRDD.filter(lambda x:x%2==0)
#print(lEven.collect())

#Reduce the sum of even number,it always return one value
# lReduce=lEven.reduce(lambda x,y:x+y)
#print(lReduce)

#flatmapp when there is an requirement to process an rdd which have certain record and it has to be transform into multiple record then 
#flatmapp is used when we need every input multiple record
#map when there one to one mapping we use map,when we need same number of outpyt records
# l=["Helo How are you","you are welcome","Welcome to university"]
# lRddd=sc.parallelize(l) #
# #print(lRddd.count())
# lFlatMap=lRddd.flatMap(lambda s : s.split(" "))
# #print(lFlatMap.count())
# lMap=lFlatMap.map(lambda s:(s,1))
# # for i in lMap.collect():
# #     print(i)
# lReduceBykey=lMap.reduceByKey(lambda x,y:x+y)
# #print(lReduceBykey.count())
# lReduceBykey=lMap.reduceByKey(add)
# print(lReduceBykey.count())
# for i in lReduceBykey.collect():
#     print(i)

# orders=sc.textFile("order.txt")
# #print(orders.take(10))
# orders.map(lambda x:x.split(" , ")[3])
# print(orders.take(10))

# orders=sc.textFile("order_items.csv")
# orderItemsMap=orders.map(lambda oi:(int(oi.split(",")[1]),float(oi.split(",")[4])))

# orderItemsMapGBK=orderItemsMap.groupByKey()

# orderRevenue=orderItemsMapGBK.map(lambda x: (x[0],sum(x[1])))
# print(orderRevenue.take(10))
























