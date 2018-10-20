<!DOCTYPE html>
	<html>
		<head>
			<link rel="stylesheet" type="text/css" href="../css/main.css">
			<title>Room - Add a room.</title>
		</head>
		<body>
			<?php
			require("../classes/Room.php");
			require("../classes/BD.php");

			use classes\Room;
			use classes\BD;

			$dbHeating = new BD();

			$rooms = $dbHeating->getAllRooms();

			$errors = [];
			$errors['nomErr'] = "";
			$errors['prenomErr'] = "";
			$errors['globalErr'] = "";
			$nomAuteur = $prenomAuteur = "";

			if ($_SERVER["REQUEST_METHOD"] == "POST") {
				if (empty($_POST["nomAuteur"])) {
					$errors['nomErr'] = "Le nom est requis.";
				} else {
					if (strlen($_POST["nomAuteur"]) < 3 || strlen($_POST["nomAuteur"]) > 20 ) {
						$errors['nomErr'] = "Le nom doit être entre 3 et 20 charactères.";
					} else {
						$nomAuteur = $_POST["nomAuteur"];
					}
				}

				if (empty($_POST["prenomAuteur"])) {
					$errors['prenomErr'] = "Le prénom est requis.";
				} else {
					if (strlen($_POST["prenomAuteur"]) < 3 || strlen($_POST["prenomAuteur"]) > 20 ) {
						$errors['prenomErr'] = "Le prénom doit être entre 3 et 20 charactères.";
					} else {
						$prenomAuteur = $_POST["prenomAuteur"];
					}
				}

				foreach ($auteurs as $auteur) {
					if ($auteur->getNomAuteur() == $_POST["nomAuteur"] && $auteur->getPrenomAuteur() == $_POST["prenomAuteur"]) {
						$errors['globalErr'] = "L'auteur existe déjà.";
					}
				}

				if($errors['nomErr'] == "" && $errors['prenomErr'] == "" && $errors['globalErr'] == "") {
					$auteur = new Auteur($_POST['nomAuteur'], $_POST['prenomAuteur']);
					$dbBibli->sauvegarderAuteur($auteur);
				}
			}
			?>
			<a href="../index.php">Go Back.</a><br /><br />
			<form method="post" action="<?php echo $_SERVER["PHP_SELF"];?>">
				<span class="error"><?php echo $errors['globalErr'];?></span><br /><br />
				Room Name: <input type="text" name="roomName"><br /><br />
				<span class="error"><?php echo $errors['roomNameErr'];?></span><br /><br />
				Maximum Temperature: <input type="text" name="prenomAuteur"><br /><br />
				<span class="error"><?php echo $errors['prenomErr'];?></span><br /><br />
				Minimum Temperature: <input type="text" name="nomAuteur"><br /><br />
				<span class="error"><?php echo $errors['nomErr'];?></span><br /><br />
				Sensor Wall Name: <input type="text" name="prenomAuteur"><br /><br />
				<span class="error"><?php echo $errors['prenomErr'];?></span><br /><br />
				Sensor Floor Name: <input type="text" name="nomAuteur"><br /><br />
				<span class="error"><?php echo $errors['nomErr'];?></span><br /><br />
				Relay Name: <input type="text" name="prenomAuteur"><br /><br />
				<span class="error"><?php echo $errors['prenomErr'];?></span><br /><br />
				<input type="submit" name="submit" value="Add">
			</form>
		</body>
</html>