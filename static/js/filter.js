
    function filtrarTareas() {
        var filtroTarea = document.getElementById("filtro-tarea").value.toLowerCase();
        var filtroDescripcion = document.getElementById("filtro-descripcion").value.toLowerCase();
        var filtroVencimiento = document.getElementById("filtro-vencimiento").value;
        var filtroCompletado = document.getElementById("filtro-completado").value;
        var filtroEstado = document.getElementById("filtro-estado").value;

        var filas = document.querySelectorAll(".table tbody tr");

        filas.forEach(function(fila) {
            var tarea = fila.querySelector("td:nth-child(1)").innerText.toLowerCase();
            var descripcion = fila.querySelector("td:nth-child(2)").innerText.toLowerCase();
            var vencimiento = fila.querySelector("td:nth-child(3)").innerText;
            var completado = fila.querySelector("td:nth-child(4)").innerText;
            var estado = fila.querySelector("td:nth-child(5)").innerText.toLowerCase();

            if (
                tarea.includes(filtroTarea) &&
                descripcion.includes(filtroDescripcion) &&
                (filtroVencimiento === "" || vencimiento === filtroVencimiento) &&
                (filtroCompletado === "" || completado === filtroCompletado) &&
                (filtroEstado === "" || estado === filtroEstado)
            ) {
                fila.style.display = "";
            } else {
                fila.style.display = "none";
            }
        });
    }

