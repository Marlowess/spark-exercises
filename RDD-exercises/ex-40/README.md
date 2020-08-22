# Order sensors by number of critical days
## Input data: a textual csv file containing the daily value of PM10 for a set of sensors
Each line of the files has the following format:<br> `sensorId,date,PM10 value (μg/m3)\n`

## Output: sensors ordered by the number of critical days
Each line of the output contains the number of days with a PM10 values greater than 50 for a sensor s and the sensorId of sensor s

---
## Example of data

### Input data
s1,2016-01-01,20.5<br>
s2,2016-01-01,30.1<br>
s1,2016-01-02,60.2<br>
s2,2016-01-02,20.4<br>
s1,2016-01-03,55.5<br>
s2,2016-01-03,52.5<br>

### Output data
2, s1 <br>
1, s2