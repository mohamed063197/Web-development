<?php
#securite
isset()//voir si la variable existe
htmlspecialchars()// annuler le fonctionnement du code html ou java script
trim()// annuler tout les espaces
// constante:
	define('Nom_Variable','VALUE');
//condition
	

//bocle
	forech(array_expression as $value){
		//commande
	}

 	forech(array_expression as $key=>$value){
		//commande

	}

//initialisation d'un tableau
	$tab1=[]
	$tab2=['un'=>1,'deux'=>2,'trois'=>3]
// condition
	condition ? action_si :action_sinon;
	
	switch (variable) {
		case 'value':
			# code...
			break;
		
		default:
			# code...
			break;
	}

//includre
require()// retourn une E_COMPILE_ERROR
include()// retourn uene E_WARNING

// fonction
function fun($arg1="value",$arg2){
	//code
	return $value;
}

#fonction a l'interieur d'un fonction
function foo(){
	function boo(){
		echo 'je suis la fonction boo';
	}
}

#il faut appeler foo apres boo sinon s'a marche pas 
foo();
boo();

#fonction variabel
#on peut mettre une fonction dans une variable

function foo(){}
$fun='foo'
$fun();

#fonction stoque dans une variable

$nom_fonction=function(){
	#code...
}

#ajouter dans un tableau
$tab[0]="mohamed"//avec indice
$tab[]='youcef'// ajouter a la fin


#affichage d'un tableau
echo '<pre>';
print_r($tab);
echo '<pre>'

# cle existe dans array
array_key_exists($cle,$tab);

# valeur existe dans un array
in_array($value,$tab);

#recuperer la clé d'une valeur dans un tableau
array_search($value, $tab);






?>