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
			require("classes/Room.php");
			require("classes/BD.php");

			use classes\Room;
			use classes\BD;

			$dbHeating = new BD();
			$rooms = $dbHeating->getAllRooms();
			?>

			<a href="forms/addRoom.php">Add a room.</a>&nbsp;
			<a href="forms/globalSetting.php">Global Configuration.</a><br /> <br />

			<?php
				foreach($rooms as $room) {
					echo '<div class="row";>';
					echo '<div class="col-4";>'.$room->getRoomName().'</div>';
					echo '<div class="col-4";>'.$room->getRoomMaxTemp().'</div>';
					echo '<div class="col-4";>'.$room->getRoomMinTemp().'</div>';
					echo '<div class="col-4";>'.$room->getRoomSensorName().'</div>';
					echo '<div class="col-4";>'.$room->getRoomSensorFloorName().'</div>';
					echo '<div class="col-4";>'.$room->getRoomRelayName().'</div>';
					echo '</div>';
					echo '<br /><br />';
				}
			?>
		</body>
</html>