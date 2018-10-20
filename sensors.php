<!DOCTYPE html>
	<html>
		<head>
			<title>Heating</title>
			<meta charset="utf-8">
			  <meta name="viewport" content="width=device-width, initial-scale=1">
			  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
			  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
			  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
		</head>
		<body>
			<?php 
			require("classes/Sensor.php");
			require("classes/BD.php");

			use classes\Sensor;
			use classes\BD;

			$dbHeating = new BD();
			$sensors = $dbHeating->getAllSensors();
			?>

			<a href="index.php">Go Back.</a>

			<?php
                echo '<div class="h1";>Sensors</div>';
                echo '<br /><br />';
				foreach($sensors as $sensor) {
					echo '<div class="row";>';
                    echo '<div class="col-4";>Nom:'.$sensor->getSensor().'</div>';
                    echo '<div class="col-4";>Température:'.$sensor->getTemperature().'</div>';
                    echo '<div class="col-4";>Humidité:'.$sensor->getHumidity().'</div>';
					echo '</div>';
					echo '<br /><br />';
				}
			?>
		</body>
</html>
