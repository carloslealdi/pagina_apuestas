// Ruta del archivo CSV
//const archivoCSV = '{% static "Municipios_por_departamento.csv" %}';

// Función para cargar los departamentos desde el archivo CSV
function cargarDepartamentos() {
    const selectDepartamentos = document.getElementById("departamentos");

    // Limpia opciones anteriores
    selectDepartamentos.innerHTML = '<option value="">Seleccione un departamento</option>';

    // Conjunto para almacenar los nombres únicos de los departamentos
    const departamentosUnicos = new Set();

    // Carga el archivo CSV
    fetch('/static/Municipios_por_departamento.csv')
        .then(response => response.text())
        .then(data => {
            // Parsea el archivo CSV
            const filas = data.split('\n');
            filas.forEach((fila, index) => {
                if (index > 0) { // Ignora la primera fila (encabezados)
                    const [departamento] = fila.split(',');
                    departamentosUnicos.add(departamento);
                }
            });

            // Agrega las opciones al selector de departamentos
            departamentosUnicos.forEach(departamento => {
                const option = document.createElement("option");
                option.value = departamento;
                option.textContent = departamento;
                selectDepartamentos.appendChild(option);
            });
        })
        .catch(error => console.error('Error al cargar el archivo CSV:', error));

}

// Función para cargar los municipios del departamento seleccionado
function cargarMunicipios() {
    const departamentoSeleccionado = document.getElementById("departamentos").value;
    const selectMunicipios = document.getElementById("municipios");

    // Limpia opciones anteriores
    selectMunicipios.innerHTML = '<option value="">Seleccione un municipio</option>';

    if (departamentoSeleccionado !== "") {
        // Carga el archivo CSV
        fetch('/static/Municipios_por_departamento.csv')
            .then(response => response.text())
            .then(data => {
                // Parsea el archivo CSV
                const filas = data.split('\n');
                filas.forEach((fila, index) => {
                    if (index > 0) { // Ignora la primera fila (encabezados)
                        const [departamento, municipio] = fila.split(',');
                        if (departamento === departamentoSeleccionado) {
                            const option = document.createElement("option");
                            option.value = municipio;
                            option.textContent = municipio;
                            selectMunicipios.appendChild(option);
                        }
                    }
                });
            })
            .catch(error => console.error('Error al cargar el archivo CSV:', error));
    }
}

// Cargar los departamentos al cargar la página
document.addEventListener("DOMContentLoaded", cargarDepartamentos);
