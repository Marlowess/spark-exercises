import sys
import os
from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql.functions import *


if __name__ == "__main__":

    # Create an instance of spark
    spark = SparkSession.builder.appName('Exercise-5').getOrCreate()

    # Current path
    absolute_path = Path().absolute()

    # Input path
    input_path = os.path.join(absolute_path, 'input.csv')

    # Input data from CSV file
    lines = spark.read.csv(input_path)

    # First get the maximum temperature
    max_temp = lines.agg({'_c2':'max'}).collect()[0][0]

    # Filter lines containing the previous temperature
    max_temp_lines = lines.where(lines._c2 == max_temp).rdd.map(lambda x: ','.join(x)).collect()

    # Print the result on the standard output
    print('\n'.join(max_temp_lines))
    
    # Stop spark
    spark.stop()