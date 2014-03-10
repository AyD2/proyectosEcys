$(document).ready(function (){
    moverLaterales();
    $(".mensaje").hide();
    $(".logo").children(".mensaje").show();
    $(".logo").children(".mensaje").css("text-align","center");
    $(".boton").click(function (){
        $(".main").onepage_scroll({
            sectionContainer: "section",
            easing: "ease",
            animationTime: 1000,
            pagination: true,
            updateURL: false,
            beforeMove: function(index) {
                $(".menuPrincipal").addClass("encabezado");
            },
            afterMove: function(index) {
            },
            loop: false,
            keyboard: true,
            responsiveFallback: false
        }) 
    });
});


function moverLaterales(){
    $(".logLateral").click(function (){
        var apachado = $(this);
        var padreApachado = $(this).offsetParent();
        var central = $(".logCentral");
        var padreCentral = $(".logo");
        var lado = "logoDerecha";

        if(!apachado.hasClass("logCentral")){
            if(padreApachado.hasClass("logoIzquierda")){
                lado = "logoIzquierda";
            }
            
            apachado.removeClass();
            apachado.addClass("logCentral");
            padreApachado.removeClass();
            padreApachado.addClass("logo");

            central.removeClass();
            central.addClass("logLateral");
            padreCentral.removeClass();
            padreCentral.addClass(lado);

            padreCentral.children(".mensaje").hide();
            padreApachado.children(".mensaje").show();
            padreApachado.children(".mensaje").css("text-align","center");

            apachado.click(moverLaterales());
            padreApachado = null;
            central.click(moverLaterales());
            padreCentral = null;
        }
    });
}


function bajar(){
    alert("asdfasdf");
    $(".main").onepage_scroll({
        sectionContainer: "section",
        easing: "ease",
        animationTime: 1000,
        pagination: true,
        updateURL: false,
        beforeMove: function(index) {},
        afterMove: function(index) {},
        loop: false,
        keyboard: true,
        responsiveFallback: false
    }); 
}
