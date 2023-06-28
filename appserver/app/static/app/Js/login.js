/* function validarYRedirigir() {
    // Validación de campos
    var nom_usuario = document.getElementById("nom_usuario").value.trim();
    var contra = document.getElementById("contra").value.trim();

    if (nom_usuario === "" || contra === "") {
        alert("Por favor, complete todos los campos.");
        return false;
    }

    // Si la validación es exitosa, abre una nueva ventana
    window.location.href = "inciado_sesion_cliente.html";
    return false; // Evita que el formulario se envíe
} */

function validarYRedirigir() {
    // Validación de campos
    var nom_usuario = document.getElementById("nom_usuario").value.trim();
    var contra = document.getElementById("contra").value.trim();
  
    if (nom_usuario === "" || contra === "") {
      // Muestra el mensaje de error en el elemento "alert"
      document.getElementById("mensajeError").innerHTML = "Por favor, complete todos los campos.";
      document.getElementById("alertaError").style.display = "block";
      return false;
    }
  
    // Si la validación es exitosa, abre una nueva ventana
    window.location.href = "inciado_sesion_cliente.html";
    return false; // Evita que el formulario se envíe
  }
  