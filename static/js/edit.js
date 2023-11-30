
function actualizarTarea(idTarea) {
    console.log("IDTAREA", idTarea);
    var row = document.getElementById(idTarea);
    var elements = fila.querySelectorAll("td");
    console.log(elements);
    var newTitle = document.getElementById("title-" + idTarea).value;
    var newDescription = document.getElementById("description-" + idTarea).value;
    var newDueDate = document.getElementById("due_date-" + idTarea).value;
    var newCompletionDate = document.getElementById("completion_date-" + idTarea).value;
    var newStatus = document.getElementById("status-" + idTarea).value;
    console.log(idTarea, newTitle, newDescription, newDueDate, newCompletionDate, newStatus);
    // Realizar la petición AJAX
    $.ajax({
        url: "/api/update",
        type: "POST",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({
            id: idTarea,
            title: newTitle,
            description: newDescription,
            dueDate: newDueDate,
            completionDate: newCompletionDate,
            status: newStatus
        }),
        success: function(response) {
            // Manejar la respuesta del servidor
            console.log(response);
            alert("Tarea actualizada correctamente");
        },
        error: function(xhr, status, error) {
            // Manejar errores de la petición AJAX
            console.error(xhr.responseText);
            alert("Error al actualizar la tarea");
        }
    });
}

document.querySelectorAll('.button').forEach(function(boton) {
    boton.addEventListener('click', function() {
        var idButton = this.getAttribute('data-id');
        actualizarTarea(idButton);
    });
});