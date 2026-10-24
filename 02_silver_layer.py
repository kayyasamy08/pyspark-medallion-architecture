# Silver Layer: Data Cleaning

from pyspark.sql.functions import col

# Read Bronze data

bronze_df = spark.table(
"workspace.default.bronze_decathlon_spark"
)

# Remove duplicate products based on objectID

silver_df = bronze_df.dropDuplicates(["objectID"])

# Remove records with missing product names

silver_df = silver_df.filter(
col("productName").isNotNull()
)

# Remove records with missing or invalid selling prices

silver_df = silver_df.filter(
col("sellingPrice").isNotNull() &
(col("sellingPrice") > 0)
)

# Save cleaned data into Silver layer

SILVER = "workspace.default.silver_decathlon_spark"

silver_df.write 
.format("delta") 
.mode("overwrite") 
.saveAsTable(SILVER)

# Display results

print("Silver Layer created successfully!")
print("Bronze records:", bronze_df.count())
print("Silver records:", silver_df.count())

display(silver_df)
