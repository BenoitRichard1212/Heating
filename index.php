<?php
// Settings
// host, user and password settings
$host = "localhost";
$user = "logger";
$password = "password";
$database = "temperatures";

//how many hours backwards do you want results to be shown in web page.
$hours = 24;

// make connection to database
$connectdb = mysqli_connect($host,$user,$password)
or die ("Cannot reach database");

// select db
mysqli_select_db($connectdb,$database)
or die ("Cannot select database");

// sql command that selects all entires from current time and X hours backwards
$sql="SELECT * FROM temperaturedata WHERE dateandtime >= (NOW() - INTERVAL $hours HOUR) order by dateandtime desc";

//NOTE: If you want to show all entries from current date in web page uncomment line below by removing //
//$sql="select * from temperaturedata where date(dateandtime) = curdate();";

// set query to variable
$temperatures = mysqli_query($connectdb,$sql);

// create content to web page
?>
<html>
<head>
<title>Environment - 4thDnet</title>
</head>

<body>
</body>
<center>Temperatures</center>
<br><br>
<table width="800" border="1" cellpadding="1" cellspacing="1" align="center">
<tr>
<th>Date</th>
<th>Sensor</th>
<th>Temperature</th>
<th>Humidity</th>
<tr>
<?php
// loop all the results that were read from database and "draw" to web page
while($temperature=mysqli_fetch_assoc($temperatures)){
echo "<tr>";
echo "<td>".$temperature['dateandtime']."</td>";
echo "<td>".$temperature['sensor']."</td>";
echo "<td>".$temperature['temperature']."</td>";
echo "<td>".$temperature['humidity']."</td>";
echo "<tr>";
}
?>
</table>
</html>

