import findspark
findspark.init()
#
from pyspark.sql import SparkSession
from pyspark import SparkContext
# from pyspark import SparkConf
from pyspark.sql import SQLContext
from pyspark.sql.types import * # Importing all SQL Types

spark = SparkSession \
    .builder \
    .appName("Dkm-Pyspark-ReadCsv-01") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# sc = SparkContext('local[*]') # This is not needed as a SparkContext is already created from the SparkSession
sqlContext = SQLContext(spark)

# Defining My Schema
MySchema = StructType() \
    .add("BankName",StringType(),True) \
    .add("TransactionDate",DateType(),True) \
    .add("TransactionOrChequeNo",StringType(),True) \
    .add("TransactionDetains",StringType(),True) \
    .add("DebitAmount",DoubleType(),True) \
    .add("CreditAmount",DoubleType(),True) \
    .add("BalanceAmount",DoubleType(),True) \
    .add("TransactionSubCategory",StringType(),True) \
    .add("TransactionMainCategory",StringType(),True) \
    .add("NotesOrRemarks",StringType(),True) \
    .add("SalaryMonth",StringType(),True)

# Read CSV File with Header and capture schema info
df = spark.read.csv("<MyLocation>\Statement-2020.csv",header="true",inferSchema="true",schema=MySchema)
df.printSchema()
df.show(10)
df.count()

# filter Debit amounts > 10K
df.filter(df.DebitAmount>=10000).count()

# filter Salary row
df.filter(df.TransactionMainCategory=='Salary').show()

# filter Salary row > 103K
df.filter((df.TransactionMainCategory=='Salary') & (df.CreditAmount>=103000)).show()

# Group By Trans Cat
df.groupBy(df.TransactionMainCategory).count().show()

# Group By Trans Cat and Sum the Amounts
df.groupBy(df.TransactionMainCategory).agg({"DebitAmount": "sum","CreditAmount": "sum","BalanceAmount": "sum"}).show()

# Group By Trans Month and Sum the Amounts and Ord by Trans Month
df.groupBy(df.TransactionDate.substr(6,2)).agg({"DebitAmount": "sum","CreditAmount": "sum","BalanceAmount": "sum"}).orderBy(df.TransactionDate.substr(6,2)).show()

# Register DF as a temp table
df.registerTempTable('MyTxnTable')
sqlContext.sql("Select * from MyTxnTable limit 10").show()

sqlContext.sql("Select distinct(MONTH(TransactionDate)) from MyTxnTable").show()

# Group By Trans Month and Sum the Amounts and Ord by Trans Month
sqlContext.sql("Select MONTH(TransactionDate),SUM(DebitAmount),SUM(CreditAmount),SUM(BalanceAmount) From MyTxnTable Group By MONTH(TransactionDate) order by 1").show()