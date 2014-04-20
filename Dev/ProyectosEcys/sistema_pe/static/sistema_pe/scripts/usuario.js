$(document).ready(function (){
    //$("#menuclase").click(menu_cursos);
    $(".div_list").click(collapse);
    $(".item_list").click(peticion_ajax);
    //$(".btnCambio").focus(peticion_ajax);
    $("#btn_cambiarp").click(cambiar_p);
    $("#btn_cambiarc").click(cambiar_c);
});


///////////////////////GENERALES
function cambiar_p(){
    pn = $("#nuevap").text();
    pa = $("#rnuevap").text();
    pv = $("#passp").text();
    var u = $("#encabezado").text().trim();
    if(pn == pa){
        console.log(pn);
        console.log(pa);
        console.log(pv);
        Dajaxice.sistema_pe.cambiar_pass(callback_cambiar_pass, {'datos':[u, pn, pv]});
    }else{
        $("#pcambiarpass > .anuncio").text('las contrasenias no coinciden!!!!');
        $("#pcambiarpass > .anuncio").show();
        $("#pcambiarpass > .anuncio").hide(8000);
    }
}

function cambiar_c(){
    cr = $("#correo_nuevo").text();
    pv = $("#pass").text();
    var u = $("#encabezado").text().trim();
    console.log(cr);
    console.log(pv);
    Dajaxice.sistema_pe.cambiar_correo(callback_cambiar_correo, {'datos':[u, cr, pv]});
}

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
        Dajaxice.sistema_pe.traer_mis_cursos(callback_mis_cursos);
    }
    if(opcion == "cambiar contraseña"){
        $(".cont").addClass("poculto");
        $("#pcambiarpass").removeClass("poculto");
        //callback_cambiar_pass('algo')
        //Dajaxice.sistema_pe.traer_mis_cursos(callback_mis_cursos);
    }
    if(opcion == ""){
        
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
        var c = $(this).data('clase');
        var args = u+" "+c;
        //console.log(args);
        Dajaxice.sistema_pe.asignar_curso(callback_asignar,{'datos':[u ,c]});
    }
    if(opcion == "desasignar"){
        var a = $(this).data('asignacion');
        console.log("esta "+a);
        Dajaxice.sistema_pe.desasignar_curso(callback_asignar,{'datos':[u ,a]});
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
}

function callback_asignar(data) {
    $("#pasignar").remove(".clase");
    $(".clase").remove();
    console.log("asignado");
    llenar_clases(data.todo, data.asignadas);
}

function callback_cambiar_pass(data) {
    $("#pcambiarpass > .anuncio").text(data.texto);
    $("#pcambiarpass > .anuncio").show();
    $("#pcambiarpass > .anuncio").hide(5000);
}
function callback_cambiar_correo(data) {
    $("#pcambiarcorreo > .anuncio").text(data.texto);
    $("#pcambiarcorreo > .anuncio").show();
    $("#pcambiarcorreo > .anuncio").hide(5000);
}


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
