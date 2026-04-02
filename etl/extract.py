from pyspark.sql import SparkSession

def extract_data():

    spark = SparkSession.builder \
        .appName("Sales Extract") \
        .getOrCreate()

    df = spark.read.csv(
        "data/sales_data.csv",
        header=True,
        inferSchema=True
    )

    return df
