<?php
# difference entre self et static

	class simple_class{

		public const  CONSTANT='valeur constante';
		public $variable="value";
		public $attribut1;
		public $attribut2;

		public $fun;
		public function __construct(){
			$this->$fun=function(){
				return #code...
			}
		}

		public function attr1_attr2(){
			return sprintf("%s %s",$this->attribut1,$this->attribut2);
		}

		public function getVariable(){
			return $this->variable;
		}


	}

	class Extends_class extends simple_class{
		public $attribut3;

		function __construct(){

			parent::__construct();
		}
		
		function getVariable(){
			parent::getVariable();
		}

		public function all_attr(){

		}


	}

	$obj1= new simple_class();
	// copier objet1
	$obj2= new $obj1;


	// appeler fonction variable
	$inst=new simple_class();
	$fun_inst=$inst->fun;
	$fun();


?>


<?php
/*classe abstraite et methode abstraite*/	
	
	#classe abstraite
	abstract class Form{
		#tout les classes fille sont obligé de redefinir la methode aire();
		abstract public function aire();

	}

	class Triangle extends Form{
		public function aire(){
			#code...
		}
	}

	class Carre extends Form{
		public function aire(){
			#code...
		}
	}


#Liskov
#si on a une classe A herite de la classe B alors on peut de instansier B et utiliser tout de A sans changer la cooherence du programmme 

	interface Form{
		public function aire();
	}
	
	class Triagle implements From{
		public function aire(){
			
		}
	}
?>