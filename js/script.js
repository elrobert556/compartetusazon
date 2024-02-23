function obtenerTr() {
    var tbody = document.getElementById('ingredientesTable');

    // Obtén todos los elementos textarea dentro del div
    var tr = tbody.getElementsByTagName('tr');

    // Variable para almacenar el ID del último textarea
    var ultimoTextareaID;

    // Itera sobre cada textarea e imprime su ID
    for (var i = 0; i < tr.length; i++) {
    var textareaID = tr[i].id;
    //console.log('Textarea ID:', textareaID);

    // Actualiza la variable con el ID del último textarea
    ultimoTextareaID = textareaID;
    }

    return ultimoTextareaID;
}

/*=============================================
SUMMERNOTE
=============================================*/
// $('#summernote').summernote({
//     height: 300
// });

/*=============================================
CARGAR INGREDIENTES EN UNA TABLA
=============================================*/
var miInput = document.getElementById('ingredientes');

// Agregar un evento de tecla (keydown)
miInput.addEventListener('keydown', function(event) {
    // Obtener el valor actual del campo de entrada
    var valorInput = miInput.value;

    // Verificar si la coma (",") está presente en el valor o si se presionó la tecla Enter (código 13)
    if ((event.keyCode === 188 && valorInput.length > 0) || event.keyCode === 13 && valorInput.length > 0) {
        // Detener el evento para evitar que se agregue la coma o Enter al campo de entrada
        event.preventDefault();

        // Dividir el valor en palabras
        var palabras = valorInput.split(',');

        // Limpiar el contenido actual del campo de entrada
        miInput.value = '';

        // Iterar sobre cada palabra
        palabras.forEach(function(palabra) {

            var tr = document.createElement('tr');

            tr.id = 1

            var tdIngrediente = document.createElement('td');
            var tdCantidad = document.createElement('td');
            var tdMedida = document.createElement('td');
            var tdBoton = document.createElement('td');

            var inputIngrediente = document.createElement('input');
            var inputCantidad = document.createElement('input');
            var img = document.createElement('img');

            inputIngrediente.id = 'nombreIngrediente'
            inputIngrediente.value = palabra

            inputCantidad.id = 'cantidadIngrediente'

            img.id = 'icono-eliminar';
            img.src = 'css/assets/delete-left-solid.svg';
            img.alt = 'Icono borrar';

            var select = document.createElement('select');
            //select.id = 

            /* OBTENER LAS OPCIONES DE MEDIDA */
            fetch('get.php', {
                method: 'GET',
                headers: {
                    'Authorization': 'bz8VVmSR5Pvb589EhAR2YUH25e3VB7'
                }
            })
            .then(response => {
                if (!response.ok) {
                throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                var opciones = data.results;

                for (var i = 0; i < opciones.length; i++) {
                    var opcion = document.createElement('option');
                    opcion.text = opciones[i].nombre_medida;
                    select.appendChild(opcion);
                }
            })
            .catch(error => {
                console.error('Hubo un problema con la petición Fetch:', error);
            });

            tdIngrediente.appendChild(inputIngrediente);
            tdCantidad.appendChild(inputCantidad);
            tdMedida.appendChild(select);
            tdBoton.appendChild(img);

            tr.appendChild(tdIngrediente);
            tr.appendChild(tdCantidad);
            tr.appendChild(tdMedida);
            tr.appendChild(tdBoton);

            img.style.cursor = 'pointer'; // Agregar cursor de puntero para indicar que es clickable

            // Agregar el evento de clic para eliminar la etiqueta
            img.addEventListener('click', function() {
                document.getElementById('ingredientesTable').removeChild(tr);
            });

            document.getElementById('ingredientesTable').appendChild(tr);
        });
    }
});