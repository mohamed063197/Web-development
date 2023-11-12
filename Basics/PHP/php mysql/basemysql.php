<?php

$requette=$bd->query("SELECT COUNT(*) AS nb FROM Livres");
$data=$requette->fetch();
$nombre_livre=$data['nb'];




$insert=$db->prepare("INSERT INTO formation ('titre','description','prix','duree') VALUES ( '".$titre."','".$description."','".$prix."','".$duree."')");