<!DOCTYPE html>
	<html>
		<head>
			<title>Rooms</title>
			<meta charset="utf-8">
			<meta name="viewport" content="width=device-width, initial-scale=1">
			<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
			<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
			<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
		</head>
		<body>
			<?php
			
			require("../Classes/Sensor.php");
			require("../Classes/Relay.php");
			require("../Classes/Room.php");
			require("../Classes/GlobalSetting.php");
			require("../Classes/BD.php");

			use Classes\Sensor;
			use Classes\Room;
			use Classes\Relay;
			use Classes\GlobalSetting;
			use Classes\BD;

			$dbHeating = new BD();

			$g_settings = $dbHeating->getAllGlobalSettings();
			$relays = $dbHeating->getAllRelays();
			$sensors = $dbHeating->getAllSensors();
			$rooms = $dbRooms->getAllRooms();

			$errors = [];
			$errors['nameErr'] = "";
			$errors['dupeErr'] = "";
			$errors['valueErr'] = "";
			$nameSetting = "";
			$valueSetting = "";

			if ($_SERVER["REQUEST_METHOD"] == "POST") {
				if (empty($_POST["nameSetting"])) {
					$errors['nameErr'] = "Le nom est requis.";
				} else {
					$nameSetting = $_POST["nameSetting"];
				}

				if (empty($_POST["valueSetting"])) {
					$errors['valueErr'] = "La valeur est requise.";
				} else {
					$valueSetting = $_POST["valueSetting"];
				}

				foreach ($g_settings as $g) {
					if ($g->getName() == $_POST["nameSetting"]) {
						$errors['dupeErr'] = "Le setting existe déjà.";
					}
				}

				if($errors['nameErr'] == "" && $errors['dupeErr'] == "") {
					$globalSetting = new GlobalSetting($_POST['nameSetting'], $_POST['valueSetting']);
					$dbHeating->addGlobalSetting($globalSetting);
					}
			}
			?>
			<a href="../index.php">Retour.</a><br /><br />
			<form method="post" action="<?php echo $_SERVER["PHP_SELF"];?>">
				<span class="error"><?php echo $errors['globalErr'];?></span><br /><br />
				<span class="error"><?php echo $errors['nameErr'];?></span><br /><br />
				<span class="error"><?php echo $errors['valueErr'];?></span><br /><br />

				Nom : <input type="text" name="nameSetting" value="">
					  <br /><br />
				Valeur : <input type="text" name="valueSetting" value="">

				<input type="submit" name="submit" value="AddSetting">
				<br /><br />
			</form>
		</body>
</html>