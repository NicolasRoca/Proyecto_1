/* document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("compra").addEventListener('submit', validar_compra); 
  });

function validar_nom_tarjeta(evento){
    evento.preventDefault();
    var nombre_tarjeta=document.getElementById('nom_tarjeta').ariaValueMax;
    if(nombre_tarjeta.length==0){
        alert('Debe ingresar un nombre para la tarjeta');
        return;
    }
} */

function validar_nombre_tarjeta(){
    console.log("Pon un nombre")
    let nombre_tarjeta=document.getElementById("nom_tarjeta").value
    console.log(nombre_tarjeta.length)
    if(nombre_tarjeta==0){
        document.getElementById("help_num_tarjeta").innerHTML="DEBE INGRESAR ALGO"
    }
}