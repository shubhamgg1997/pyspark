'''JOIN POSTCODE WITH COUNTRY AND CITY WITH BROADCAST VAIABLE'''

from pyspark.sql import SparkSession

if __name__=="__main__":
    session=SparkSession.builder.appName("employee").master("local[1]").getOrCreate()

    employeeRecord=session.read.option("header","true").csv("employee.csv")
    postcodeRecord=session.read.option("header","true").csv("city.csv")

    # print("=== Employee Record Table===")
    # employeeRecord.select("employee_id","employee_name","Postcode","number").show()

    # print("===Postcode===")
    # postcodeRecord.select("Postcode","City","Country").show()


    joined=employeeRecord.join(postcodeRecord,employeeRecord["Postcode"]==postcodeRecord["Postcode"],"leftouter")
    

    joined.show()
