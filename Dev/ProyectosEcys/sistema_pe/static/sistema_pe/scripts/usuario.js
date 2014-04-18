$(document).ready(function (){
    //$("#menuclase").click(menu_cursos);
    $(".div_list").click(collapse);
    $(".item_list").click(peticion_ajax);
    $(".btnCambio").focus(function () {
        $(this).empti();
    });
});


///////////////////////GENERALES
function peticion_ajax(){
    objeto = $(this);
    opcion = objeto.text().toLowerCase().trim();
    var u = $("#encabezado").text().trim();
    console.log(u);
    if(opcion == "gestion de cursos"){
        $(".cont").addClass("poculto");
        $("#pasignar").removeClass("poculto");
        Dajaxice.sistema_pe.traer_cursos(callback_cursos, {'carnet':u});
    }
    if(opcion == "mis cursos"){
        $(".cont").addClass("poculto");
        $("#pcursos").removeClass("poculto");
        //Dajaxice.sistema_pe.traer_mis_cursos(callback_mis_cursos);
    }
    if(opcion == "cambiar contraseña"){
        $(".cont").addClass("poculto");
        $("#pcambiarpass").removeClass("poculto");
        //Dajaxice.sistema_pe.traer_mis_cursos(callback_mis_cursos);
    }
    if(opcion == "cambiar correo"){
        $(".cont").addClass("poculto");
        $("#pcambiarcorreo").removeClass("poculto");
        Dajaxice.sistema_pe.traer_mis_cursos(callback_mis_cursos);
    }
    if(opcion == "commit"){
        $(".cont").addClass("poculto");
        $("#pcommit").removeClass("poculto");
        Dajaxice.sistema_pe.traer_mis_cursos(callback_mis_cursos);
    }
    if(opcion == "asignar"){
        alert($(this).data('clase'));
        //Dajaxice.sistema_pe.asignar(callback_asignar,{'carnet':c ,'clase':5});
    }
    if(opcion == "desasignar"){
        alert($(this).data('clase'));
        var c = $(this).data('clase');

        Dajaxice.sistema_pe.asignar(callback_asignar,{'carnet':u ,'clase':c});
    }
}


//////////////////////CALLBACKS AJAX

function callback_repos(data) {
    alert(data.repos);
}

function callback_cursos(data) {
    $("#pasignar").remove(".clase");
    $(".clase").remove();
    llenar_clases(data.todo, data.asignadas);
    $(".btn_asignar").click(peticion_ajax);
}

function callback_asignar(data) {
    $("#pasignar").remove(".clase");
    $(".clase").remove();
    llenar_clases(data.todo, data.asignadas);
    $(".btn_asignar").click(peticion_ajax);
}



///////////////////////GRAFICOS
function llenar_clases(lista_todo, lista_asignacion){
    var todo = lista_todo;
    var asignacion = lista_asignacion;
    var existe = false;
    for(var i = 0; i < todo.length; i++){
        for(var j = 0; j < asignacion.length; j++){
            if(todo[i].pk == asignacion[j].fields.id_Clase){
                existe = true;
                console.log("un asignado "+todo[i].fields.nombre) 
                break; 
            }
        }
        if(existe){
            var cont = "<div class=\"clase\">"+
                            "<div class=\"desc\">"+todo[i].fields.nombre+"   "+todo[i].fields.seccion+"</div><!--"+
                            "--><div class=\"btn_deasignar\" data-clase=\""+todo[i].pk+"\">"+
                            "<div class=\"triangulo_deasig\"> </div>&nbsp;&nbsp;Desasignar</div>"+
                        "</div>";
            console.log(cont);
            $("#pasignar").append(cont);
            existe = false;
        }else{
            //no asignado
            var cont = "<div class=\"clase\">"+
                            "<div class=\"desc\">"+todo[i].fields.nombre+"   "+todo[i].fields.seccion+"</div><!--"+
                            "--><div class=\"btn_asignar\" data-clase=\""+todo[i].pk+"\"> &nbsp;&nbsp;Asignar <div class=\"triangulo_asig\"></div></div>"+
                        "</div>";
            console.log(cont);
            $("#pasignar").append(cont);
            existe = false;
            $("#pasignar").append("");
        }
    }
    $(".btn_asignar").click(peticion_ajax);
    $(".btn_deasignar").click(peticion_ajax);
}

function collapse() {
    opcion = $(this).text().toLowerCase().trim();
    $("#list_"+opcion+"> .item_list").toggleClass("oculto");
}

function uncollapse() {
    opcion = $(this).text().toLowerCase().trim();
    $("#list_"+opcion+">.item_list").show(200);
}
