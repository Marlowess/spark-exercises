import sys
import os
from pathlib import Path

from pyspark.sql import SparkSession


if __name__ == "__main__":

    # Create an instance of spark
    spark = SparkSession.builder.appName('Exercise-3').getOrCreate()

    # Current path
    absolute_path = Path().absolute()

    # Input path
    input_path = os.path.join(absolute_path, 'input.csv')

    # Input data from CSV file
    lines = spark.read.csv(input_path)

    # Get max temperature
    max_temp = lines.agg({"_c2":"max"}).collect()[0][0]

    # Print the result on the standard output
    print(max_temp)
    
    # Stop spark
    spark.stop()