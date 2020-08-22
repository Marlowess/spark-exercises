# Top-k most critical sensors
## Input
1) A testual csv file containing the daily value of PM10 for a set of sensors<br>
Each line of the files has the following format:<br> `sensorId,date,PM10 value (μg/m3)\n`
<br><br>
The value of k <br>
It is an argument of the application

## Output: sensors ordered by the number of critical days
Data containing the top-k critical sensors<br>
The "criticality" of a sensor is given by the number of days with a PM10 values greater than 50<br>
Each line contains the number of critical days and the sensorId

---
## Example of data

### Input data
s1,2016-01-01,20.5<br>
s2,2016-01-01,30.1<br>
s1,2016-01-02,60.2<br>
s2,2016-01-02,20.4<br>
s1,2016-01-03,55.5<br>
s2,2016-01-03,52.5<br>

k = 1<br>

### Output data
2, s1