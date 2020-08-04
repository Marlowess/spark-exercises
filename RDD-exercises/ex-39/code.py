import sys
import os
from pathlib import Path

from pyspark.sql import SparkSession
from operator import add

def split_data(line):
    """
    Split each line into columns
    """
    data = str.split(line, ',')
    return [data[0], data[1]]

def filter_by_threshold(line):
    """
    Just a filter
    """
    temp = float(str.split(line, ',')[2])
    return temp > 50


if __name__ == "__main__":

    # Create an instance of spark
    spark = SparkSession.builder.appName('Exercise-39').getOrCreate()

    # Current path
    absolute_path = Path().absolute()

    # Input path
    input_path = os.path.join(absolute_path, 'input.csv')

    # Get a spark context
    sc = spark.sparkContext

    # Input data from CSV file
    lines = sc.textFile(input_path)

    # Filter out all readings below threshold 50 and return (sensorId, date)
    lines_above = lines.filter(filter_by_threshold).map(split_data)

    # Map each reading with a counter
    lines_above_by_key = lines_above.groupByKey().mapValues(list).collect()

    # Print the result on the standard output
    print(lines_above_by_key)
    
    # Stop spark
    spark.stop()