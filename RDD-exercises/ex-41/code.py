import sys
import os
from pathlib import Path
from operator import add

from pyspark.sql import SparkSession

def check_argv_value(vals):
    if len(vals) <= 1:
        print("ERR: Please provide a valid value for K", file=sys.stderr)   
        exit(-1)
    try:
        k = int(vals[1])
    except ValueError:
        print("ERR: {} is not a valid value for K".format(vals[1]), file=sys.stderr)   
        exit(-1)
    return k

def split_data(line):
    """
    Returns sensorId,1 of readings with temperature above 50
    """
    data = str.split(line, ',')
    key = data[0]  
    temperature = float(data[2])  
    return [key, 1 if temperature > 50 else 0]

def swap_parts(line):
    """
    Swap key and value and return
    """
    return (line[1], line[0])

if __name__ == "__main__":

    # Check the number of command-line parameters
    k = check_argv_value(sys.argv)

    # Create an instance of spark
    spark = SparkSession.builder.appName('Exercise-41').getOrCreate()

    # Current path
    absolute_path = Path().absolute()

    # Input path
    input_path = os.path.join(absolute_path, 'input.csv')

    # Get a spark context
    sc = spark.sparkContext

    # Input data from CSV file
    lines = sc.textFile(input_path)

    # Filter out all readings below threshold 50 and return (sensorId, 1)
    lines_key_value = lines.map(split_data)

    # For each sensorId count how many lines there are
    # lines_above_by_key = lines_key_value.groupByKey().mapValues(map_values_func).sortByKey().collect()
    sensors_counter = lines_key_value.reduceByKey(add).map(swap_parts).sortByKey(ascending=False).collect()

    # Print the result on the standard output
    print(sensors_counter[:k])
    
    # Stop spark
    spark.stop()