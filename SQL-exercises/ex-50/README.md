## Input
A CSV file containing a list of profiles<br>
- Header: `name,age,gender`
- Each line of the file contains the information about one user

## Output
A csvfile containing one single column called “name_surname” of type String<br>
`name_surname= name+""+surname`

---
## Example of data

### Input data
name,surname,age<br>
Paolo,Garza,42<br>
Luca,Boccia,41<br>
Maura,Bianchi,16<br>

### Expected output
name,surname,age<br>
Paolo,Garza,[40-49]<br>
Luca,Boccia,[40-49]<br>
Maura,Bianchi,[10-19]