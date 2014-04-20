$(document).ready(function (){
    //$("#menuclase").click(menu_cursos);
    $(".div_list").click(collapse);
    $(".item_list").click(peticion_ajax);
    //$(".btnCambio").focus(peticion_ajax);
    $("#btn_cambiarp").click(cambiar_p);
    $("#btn_cambiarc").click(cambiar_c);
});


///////////////////////GENERALES

function peticion_ajax(){
    objeto = $(this);
    opcion = objeto.text().toLowerCase().trim();
    var u = $("#encabezado").text().trim();

    console.log(u);
    if(opcion == "crear proyecto"){
        $(".cont").addClass("poculto");
        $("#pcrearproyecto").removeClass("poculto");
        Dajaxice.sistema_pe.traer_proyectos(callback_crear_proyecto, {'carnet':u});
    }
    if(opcion == "mis proyectos"){
        $(".cont").addClass("poculto");
        $("#pmisproyectos").removeClass("poculto");
        Dajaxice.sistema_pe.traer_proyectos(callback_proyectos, {'carnet':u});
    }
    if(opcion == "agregar contenido"){
        $(".cont").addClass("poculto");
        $("#pagregarc").removeClass("poculto");
        Dajaxice.sistema_pe.traer_proyectos(callback_proyectos, {'carnet':u});
    }
    if(opcion == "ver contenido anterior"){
        $(".cont").addClass("poculto");
        $("#pvercontenido").removeClass("poculto");
        Dajaxice.sistema_pe.traer_proyectos(callback_proyectos, {'carnet':u});
    }
}


//////////////////////CALLBACKS AJAX



///////////////////////GRAFICOS
function llenar_clases(lista_todo, lista_asignacion){
    var todo = lista_todo;
    var asignacion = lista_asignacion;
    var existe = false;
    for(var i = 0; i < todo.length; i++){
        var esta_asignacion = null;
        for(var j = 0; j < asignacion.length; j++){
            if(todo[i].pk == asignacion[j].fields.id_Clase){
                existe = true;
                esta_asignacion = asignacion[j].pk;
                console.log("un asignado "+esta_asignacion)
                break; 
            }
        }
        if(existe){
            var cont = "<div class=\"clase\">"+
                            "<div class=\"desc\">"+todo[i].fields.nombre+"   "+todo[i].fields.seccion+"</div><!--"+
                            "--><div class=\"btn_deasignar\" data-asignacion=\""+esta_asignacion+"\">"+
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
