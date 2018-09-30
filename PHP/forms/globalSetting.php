<!DOCTYPE html>
	<html>
		<head>
			<link rel="stylesheet" type="text/css" href="../css/main.css">
			<title>Bibliothèque - Ajoutez un livre.</title>
		</head>
		<body>
			<?php
			require("../classes/Auteur.php");
			require("../classes/Livre.php");
			require("../classes/Bibliotheque.php");
			require("../classes/BD.php");

			use classes\Auteur;
			use classes\Livre;
			use classes\Bibliotheque;
			use classes\BD;

			$dbBibli = new BD();

			$bibli = $dbBibli->chargerBibliotheque();

			$auteurs = $dbBibli->chargerAuteurs();
			$auteurAjout = "";

			$livres = $bibli->getLivres();

			$errors = [];
			$errors['titreErr'] = "";
			$errors['globalErr'] = "";
			$titreLivre = "";

			if ($_SERVER["REQUEST_METHOD"] == "POST") {
				if (empty($_POST["titreLivre"])) {
					$errors['titreErr'] = "Le titre est requis.";
				} else {
					$titreLivre = $_POST["titreLivre"];
				}

				foreach ($livres as $livre) {
					if ($livre->getTitreLivre() == $_POST["titreLivre"]) {
						$errors['globalErr'] = "Le livre existe déjà.";
					}
				}

				if($errors['titreErr'] == "" && $errors['globalErr'] == "") {
					foreach($auteurs as $key => $auteur) {
									if($key == $_POST['auteur']) {
									$auteurAjout = new Auteur($auteur->getNomAuteur(), $auteur->getPrenomAuteur());
								}
					$livre = new Livre($_POST['titreLivre'], $auteurAjout, $_POST['note']);
					$dbBibli->sauvegarderLivre($livre);
					}
				}
			}
			?>
			<a href="../index.php">Retour.</a><br /><br />
			<form method="post" action="<?php echo $_SERVER["PHP_SELF"];?>">
				<span class="error"><?php echo $errors['globalErr'];?></span><br /><br />
				Titre : <input type="text" name="titreLivre"><br /><br />
				<span class="error"><?php echo $errors['titreErr'];?></span><br /><br />

				Auteur : <select name="auteur">
							<?php
								foreach($auteurs as $key => $auteur) {
									echo '<option value="', $key,'">';
									echo $auteur->getNomAuteur(), ', ', $auteur->getPrenomAuteur();
									echo '</option>';   
								}
							?>
						 </select><br /><br />
				Note :   <select name="note">
								<option value="1">1</option>
								<option value="2">2</option>
								<option value="3">3</option>
								<option value="4">4</option>
								<option value="5">5</option>	
						  </select><br /><br />

				<input type="submit" name="submit" value="Enregistrer">
			</form>
		</body>
</html>