function mostrarPopup(contenido, color) {
    var popupContainer = document.getElementById('popup-container');
    var popupContent = document.getElementById('popup-content');

    popupContent.innerHTML = contenido;
    popupContent.style.color = color;

    popupContainer.classList.remove('hidden');
}

function cerrarPopup() {
    var popupContainer = document.getElementById('popup-container');
    popupContainer.classList.add('hidden');
}

function goBack() {
    window.history.back();
}
