import sys
import os
from pathlib import Path

from pyspark.sql import SparkSession

def split_data(line):
    """
    Return the temperature of each line
    """
    data = str.split(line, ',')
    return data[2]


if __name__ == "__main__":

    # Create an instance of spark
    spark = SparkSession.builder.appName('Exercise-33').getOrCreate()

    # Current path
    absolute_path = Path().absolute()

    # Input path
    input_path = os.path.join(absolute_path, 'input.csv')

    # Get a spark context
    sc = spark.sparkContext

    # Input data from CSV file
    lines = sc.textFile(input_path)

    # Get temperatures only
    temperatures = lines.map(split_data)

    # Get the top-3 temperatures
    top_3 = temperatures.top(3)

    # Print the temperatures
    print('\n'.join(top_3))
    
    # Stop spark
    spark.stop()