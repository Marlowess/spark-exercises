import sys
import os
from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql.functions import *


if __name__ == "__main__":

    # Create an instance of spark
    spark = SparkSession.builder.appName('Exercise-4').getOrCreate()

    # Current path
    absolute_path = Path().absolute()

    # Input path
    input_path = os.path.join(absolute_path, 'input.csv')

    # Input data from CSV file
    lines = spark.read.csv(input_path)

    # Get top-3 temperatures
    top_k_temps = lines.orderBy(desc('_c2')).select('_c2').take(3)

    # Print the result on the standard output
    print('\n'.join(r._c2 for r in top_k_temps))
    
    # Stop spark
    spark.stop()