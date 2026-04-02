from pyspark.sql.functions import col, sum

def transform_data(df):

    df_clean = df.dropna()

    df_clean = df_clean.withColumn(
        "total_sales",
        col("price") * col("quantity")
    )

    daily_sales = df_clean.groupBy("order_date") \
        .agg(sum("total_sales").alias("daily_sales"))

    top_products = df_clean.groupBy("product") \
        .agg(sum("total_sales").alias("product_sales"))

    customer_sales = df_clean.groupBy("customer_id") \
        .agg(sum("total_sales").alias("customer_sales"))

    return daily_sales, top_products, customer_sales
