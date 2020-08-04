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
    spark = SparkSession.builder.appName('Exercise-34').getOrCreate()

    # Current path
    absolute_path = Path().absolute()

    # Input path
    input_path = os.path.join(absolute_path, 'input.csv')

    # Get a spark context
    sc = spark.sparkContext

    # Input data from CSV file
    lines = sc.textFile(input_path)

    # First get the maximum temperature
    max_temp = lines.map(split_data).top(1)[0]

    # Filter lines containing the previous temperature
    max_temp_lines = lines.filter(lambda x: split_data(x) == max_temp).collect()

    # Print the result on the standard output
    print('\n'.join(max_temp_lines))
    
    # Stop spark
    spark.stop()