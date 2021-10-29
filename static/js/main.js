function validar_formulario(){
    var email = document.formRegistro.email;   

    var formato_email = /^\w+([\.-]?\w+)@w+([\.-]?w+)(\.\w{2,3})+$/;
    if (!email.value.match(formato_email)){
        alert("¡Debes ingresar un email valido!");
        email.focus();
        return false;
    } 
}