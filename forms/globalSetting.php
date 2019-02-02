<!DOCTYPE html>
	<html>
		<head>
			<title>Global Settings</title>
			<meta charset="utf-8">
			<meta name="viewport" content="width=device-width, initial-scale=1">
			<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
			<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
			<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
		</head>
		<body>
			<?php
			require("../Classes/GlobalSetting.php");
			require("../Classes/BD.php");

			use Classes\GlobalSetting;
			use Classes\BD;

			$dbHeating = new BD();

			$g_settings = $dbHeating->getAllGlobalSettings();

			$errors = [];
			$errors['nameErr'] = "";
			$errors['dupeErr'] = "";
			$nameSetting = "";

			if ($_SERVER["REQUEST_METHOD"] == "POST") {
				if (empty($_POST["nameSetting"])) {
					$errors['nameErr'] = "Le nom est requis.";
				} else {
					$nameSetting = $_POST["nameSetting"];
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
				Titre : <input type="text" name="nameSetting"><br /><br />
				<span class="error"><?php echo $errors['nameErr'];?></span><br /><br />

				Nom : <input type="text" name="nameSetting" value="Entrer le nom.">
					  <br /><br />
				Valeur : <input type="text" name="valueSetting" value="Entrer la valeur.">

				<input type="submit" name="submit" value="AddSetting">
				<br /><br />
			</form>
		</body>
</html>