import sys
import os
from pathlib import Path

from pyspark.sql import SparkSession


if __name__ == "__main__":

    # Create an instance of spark
    spark = SparkSession.builder.appName('Exercise-31').getOrCreate()

    # Current path
    absolute_path = Path().absolute()

    # Input path
    input_path = os.path.join(absolute_path, 'input.txt')

    # Output path
    output_path = os.path.join(absolute_path, 'output')

    # Input data    
    lines = spark.read.text(input_path).rdd.map(lambda x: x[0])

    # Filter out data not containing the work 'google'
    lines_w_google = lines.filter(lambda x: 'google' in x)

    # Take unique IPs
    unique_ips = lines_w_google.map(lambda x: str.split(x, ' ')[0]).distinct()

    # Save data on the output file
    unique_ips.coalesce(1).saveAsTextFile(output_path)
    
    # Stop spark
    spark.stop()