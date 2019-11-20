'''Write a program  which take a list of list and give result of 
# all list'''
from pyspark import SparkContext
sc = SparkContext("local", "list app")
list1=[[1,2,3],[4,5,6],[7,8,9]]
list2=sc.parallelize(list1)
list3=list2.reduce(lambda x,y: x+y)
print(list3)

