import sys
import os
from pathlib import Path
from operator import add

from pyspark.sql import SparkSession

def perform_analysis_dataframe(df, output_path):
    """
    Perform this analysis by only using Dataframe APIs
    """
    result_df = df.filter(df.gender == 'male').select('name', 'age').withColumn('age', df.age + 1).sort(df.age.desc(), df.name.asc())
    result_df.repartition(1).write.csv(output_path, mode='overwrite')
    

def perform_analysis_sql(session, df, output_path):
    """
    Perform this analysis by using SQL queries and tempViews    
    """
    
    # Create a temporary view associated with the input data
    df.createOrReplaceTempView("users")

    # Submit SQL queries on the view
    df_2 = session.sql("select name, age+1 as age FROM users WHERE gender = 'male' ORDER BY age DESC, name ASC;") 
    df_2.repartition(1).write.csv(output_sql_path, mode='overwrite')  

    # Drop the view
    session.catalog.dropTempView("users")

if __name__ == "__main__":

    # Create an instance of spark
    spark = SparkSession.builder.appName('Exercise-47').getOrCreate()

    # Current path
    absolute_path = Path().absolute()

    # Input path
    input_path = os.path.join(absolute_path, 'input.csv')

    # Output paths
    output_df_path = os.path.join(absolute_path, 'result_dataframe_mode')
    output_sql_path = os.path.join(absolute_path, 'result_sql_mode')

    # Load input data into a dataframe
    df = spark.read.csv(input_path, header=True, inferSchema=True)

    # Perform the analysis by using the dataframe
    perform_analysis_dataframe(df, output_df_path)

    # Perform the analysis by using SQL queries
    perform_analysis_sql(spark, df, output_sql_path)

    # Stop Spark execution
    spark.stop()