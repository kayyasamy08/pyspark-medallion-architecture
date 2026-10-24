# Bronze Layer: Raw Data Ingestion

from pyspark.sql.functions import current_timestamp

# Source table

SOURCE = "workspace.default.decathlon_21439"

# Bronze table

BRONZE = "workspace.default.bronze_decathlon_spark"

# Read raw data from source

df_raw = spark.table(SOURCE)

# Add ingestion timestamp

bronze_df = df_raw.withColumn(
"ingestion_timestamp",
current_timestamp()
)

# Write data into Bronze Delta table

bronze_df.write 
.format("delta") 
.mode("overwrite") 
.saveAsTable(BRONZE)

# Display Bronze data

print("Bronze Layer created successfully!")
print("Total records:", bronze_df.count())

display(spark.table(BRONZE))
