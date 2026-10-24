# Gold Layer: Business Summary

from pyspark.sql.functions import count, avg, min, max, round

# Read Silver table

silver_df = spark.table(
"workspace.default.silver_decathlon_spark"
)

# Create brand-wise summary

gold_df = silver_df.groupBy("brand").agg(
count("*").alias("total_products"),
round(avg("sellingPrice"), 2).alias("average_price"),
min("sellingPrice").alias("minimum_price"),
max("sellingPrice").alias("maximum_price")
)

# Save Gold table

GOLD = "workspace.default.gold_decathlon_summary_spark"

gold_df.write 
.format("delta") 
.mode("overwrite") 
.saveAsTable(GOLD)

# Display results

print("Gold Layer created successfully!")
print("Total brands:", gold_df.count())

display(gold_df)
