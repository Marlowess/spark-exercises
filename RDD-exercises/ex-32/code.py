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
    spark = SparkSession.builder.appName('Exercise-32').getOrCreate()

    # Current path
    absolute_path = Path().absolute()

    # Input path
    input_path = os.path.join(absolute_path, 'input.csv')

    # Get a spark context
    sc = spark.sparkContext

    # Input data from CSV file
    lines = sc.textFile(input_path)

    # Extract temperature from sensors data
    temperatures = lines.map(split_data)

    # Take the maximum temperature
    max_temp = temperatures.reduce(lambda x,y : x if x > y else y)

    # Print the result on the standard output
    print(max_temp)
    
    # Stop spark
    spark.stop()