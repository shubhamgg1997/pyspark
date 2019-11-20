'''Broadcast variable are used to save the copy of data across all nodes.
This variable are stored in cached on all te machines.
It is a variable which has an attribute called value which store data and is used
to return a broadcost class 

It is used normally for reading data across all worker nodes
'''
from pyspark import SparkContext
sc=SparkContext("local","Broadcast app")
words_new=sc.broadcast(["scala","java","hadoop","spark","akkka"])
data=words_new.value
print("Stored data -> %s"%(data))
elem=words_new.value[2]
print("Printing a particular element in RDD -> %s" % (elem))

