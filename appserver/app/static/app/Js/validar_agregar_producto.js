const formulario = document.getElementById("formulario");
const mensajeAprobado = document.getElementById("mensajeAprobado");

formulario.addEventListener("submit", (e) => {
    e.preventDefault();
    let camposValidos = true;

    const inputs = formulario.querySelectorAll("input, select");

    inputs.forEach((input) => {
        const mensajeError = input.parentNode.querySelector(".error");

        if (mensajeError) {
            mensajeError.remove();
        }

        if (!input.checkValidity()) {
            camposValidos = false;
            const error = document.createElement("span");
            error.className = "error";
            error.textContent = input.validationMessage;
            input.parentNode.appendChild(error);
        }
    });

    if (camposValidos) {
        mensajeAprobado.style.display = "block";
    } else {
        mensajeAprobado.style.display = "none";
    }
});
