import sys
import os
from pathlib import Path

from pyspark.sql import SparkSession

def split_data(line):
    """
    Split each line into columns
    """
    data = str.split(line, ',')
    return [data[0], data[2]]


if __name__ == "__main__":

    # Create an instance of spark
    spark = SparkSession.builder.appName('Exercise-37').getOrCreate()

    # Current path
    absolute_path = Path().absolute()

    # Input path
    input_path = os.path.join(absolute_path, 'input.csv')

    # Get a spark context
    sc = spark.sparkContext

    # Input data from CSV file
    lines = sc.textFile(input_path)

    # Map each line to a pair (sensorID, temp)
    sensor_temp = lines.map(split_data)

    # Select the maximum temperature for each sensor
    max_temp_by_sensor = sensor_temp.reduceByKey(lambda x,y : x if x > y else y).collect()

    # Print the result on the standard output
    print(max_temp_by_sensor)
    
    # Stop spark
    spark.stop()