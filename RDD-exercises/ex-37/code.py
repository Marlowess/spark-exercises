import sys
import os
from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql.functions import *


if __name__ == "__main__":

    # Create an instance of spark
    spark = SparkSession.builder.appName('Exercise-37').getOrCreate()

    # Current path
    absolute_path = Path().absolute()

    # Input path
    input_path = os.path.join(absolute_path, 'input.csv')

    # Input data from CSV file
    lines = spark.read.csv(input_path)

    # Group by sensorId and compute the max value for each group
    max_temp_by_sensor = lines.groupBy(['_c0']).agg({'_c2':'max'}).rdd.map(lambda x: ','.join(x)).collect()

    # Print the result on the standard output
    print(max_temp_by_sensor)
    
    # Stop spark
    spark.stop()