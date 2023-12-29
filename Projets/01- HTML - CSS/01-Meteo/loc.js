/* Affichage de l'heure */
date=new Date()
document.getElementById("h").innerHTML=date.getHours()+":"+date.getMinutes() ;

function getUrl(lat, long, langue="fr", units="metric"){
    /*Recuperation des informations Meteo*/
    let root="https://api.openweathermap.org/data/2.5/weather?"
    let p={
        "lat":lat,
        "lon":long,
        "lang":langue,
        "units":units,
        "appid":"c27a97a9fadcef115d6f6af59bfdb304"  
    };
    let tmp_url=""
    for(const [key, value] of Object.entries(p)){
        tmp_url=tmp_url+"&"+key+"="+value
    } 
   
    return root+tmp_url.substring(1,tmp_url.length)
}

/* Recuperation de la latitude et la longitude */
lat=0
long=0
lang="fr"
adresse=""
description=""
tempMax=""
tempMin=""
temp=""
humidity=""
pressure=""
wind=""
cookie=false


/* coordonnees */
function coordonnees(pos) {
    var crd = pos.coords;
    lat = crd.latitude.toFixed(2);
    long = crd.longitude.toFixed(2);
    var url=getUrl(lat, long)

    fetch(url)  
        .then(function(resp) { return resp.json() }) // Convert data to json
        .then(function(res_data) {
      
            adresse=res_data["name"]
            description=res_data["weather"][0]['description']
            tempMax=res_data["main"]['temp_max']
            tempMin=res_data["main"]['temp_min']
            temp=res_data["main"]['temp']
            humidity=res_data["main"]['humidity']
            pressure=res_data["main"]['pressure']
            wind=res_data["wind"]['speed']

            console.log(res_data)
            console.log(res_data["name"])

            /* Attribution des données */
            document.getElementById("pos").innerHTML=adresse
            document.getElementById("temp").innerHTML=temp.toFixed(0)
            document.getElementById("temp_min").innerHTML=tempMin.toFixed(0)+"°"
            document.getElementById("temp_max").innerHTML=tempMax.toFixed(0)+"°"
            document.getElementById("humidity").innerHTML=humidity+"%"
            document.getElementById("wind").innerHTML=wind.toFixed(0)
            document.getElementById("description").innerHTML=description

        })
        .catch(function() {
        // catch any errors
        });

}

navigator.geolocation.getCurrentPosition(coordonnees);
lang=navigator.language 
cookie=navigator.cookieEnabled 
console.log("Cookies active "+cookie)




/*----------------------------------------------------------------*/
function celToFah(d){
    return (d*1.8+32)
}

  /* Affichage de la Meteo */
  const farad=document.getElementById("farad");
  const degree=document.getElementById("degre");

  farad.addEventListener('click',function(){
      // Recuperer la valeur en farad Python (temperature, min, max)
      // Touse les modifier
              
     
      document.getElementById("temp").innerHTML=celToFah(temp).toFixed(0)
      document.getElementById("temp_min").innerHTML=celToFah(tempMin).toFixed(0)+"°"
      document.getElementById("temp_max").innerHTML=celToFah(tempMax).toFixed(0)+"°"


      this.setAttribute("class","degre active")
      degree.setAttribute("class","degre")
      
  })


  degree.addEventListener('click',function(){
      // Recuperer la valeur en degre Python (temperature, min, max)
      // Touse les modifier
      document.getElementById("temp").innerHTML=temp.toFixed(0)
      document.getElementById("temp_min").innerHTML=tempMin.toFixed(0)+"°"
      document.getElementById("temp_max").innerHTML=tempMax.toFixed(0)+"°"
      this.setAttribute("class","degre active")
      farad.setAttribute("class","degre")
      
  })








  
