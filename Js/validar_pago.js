document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("compra").addEventListener('submit', function(evento) {
      evento.preventDefault();
      validar_nom_tarjeta();
      redireccionar();
    });
  });
  
  function validar_nom_tarjeta() {
    var nombre_tarjeta = document.getElementById('nom_tarjeta').value;
    if (nombre_tarjeta.length == 0) {
      alert('Debe ingresar un nombre para la tarjeta');
      return false;
    }
    return true;
  } 
  
  function redireccionar() {
    window.location.href = "pago_realizada.html";
  }
  