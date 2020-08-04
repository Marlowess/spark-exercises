import sys
import os
from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql.functions import *


if __name__ == "__main__":

    # Create an instance of spark
    spark = SparkSession.builder.appName('Exercise-36').getOrCreate()

    # Current path
    absolute_path = Path().absolute()

    # Input path
    input_path = os.path.join(absolute_path, 'input.csv')

    # Input data from CSV file
    lines = spark.read.csv(input_path)

    # Select _c2 column only and compute the mean
    mean_temp = lines.agg({'_c2':'avg'}).collect()[0][0]

    # Print the result on the standard output
    print('%2.2f' % mean_temp)
    
    # Stop spark
    spark.stop()