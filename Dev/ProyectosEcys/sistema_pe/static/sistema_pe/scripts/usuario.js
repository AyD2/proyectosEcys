$(document).ready(function (){
    alert("mierda");
    $("#menuclase").click(menu_cursos);
});


function menu_mis_cursos(){
    Dajaxice.sistema_pe.traer_mis_cursos(callback_mis_cursos);
}

function menu_cursos(){
    Dajaxice.sistema_pe.traer_cursos(callback_cursos);
}

function menu_mis_enunciados(){
    Dajaxice.sistema_pe.traer_enunciados(callback_enunciados);
}

//////////////////////CALLBACKS AJAX

function callback_repos(data) {
    alert(data.repos);
}

function callback_cursos(data) {
    alert(data[0].fields.nombre);

}

function callback_enunciados(data) {
    alert(data);
}
