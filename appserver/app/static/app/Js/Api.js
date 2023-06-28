function generateRandomUserImage() {
    const url = "https://randomuser.me/api/";

    fetch(url)
        .then((response) => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error(`Error: \${response.status}`);
            }
        })
        .then((user_data) => {
            displayUserImage(user_data);
        })
        .catch((error) => {
            console.error(error);
        });
}

function displayUserImage(user_data) {
    const image_url = user_data.results[0].picture.large;

    document.getElementById("image").src = image_url;
}

// Llama a la función al cargar la página
generateRandomUserImage();
