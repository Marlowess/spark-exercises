# Critical dates analysis
## Input data: a textual csv file containing the daily value of PM10 for a set of sensors
Each line of the files has the following format:<br> `sensorId,date,PM10 value (μg/m3)\n`

## Output: a line for each sensor on the standard output
Each line contains a sensorIdand the list of dates with a PM10 values greater than 50 for that sensor.

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
(s1, [2016-01-02, 2016-01-03])<br>
(s2, [2016-01-03])