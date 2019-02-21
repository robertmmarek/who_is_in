window.addEventListener('load', function(){
    let form = document.getElementById('repeatPasswordForm');
    let password = document.getElementById('passwordInput');
    let passwordRepeat = document.getElementById('repeatPasswordInput');

    passwordRepeat.addEventListener('input', function(event){
        if(password.value != passwordRepeat.value)
        {
            passwordRepeat.setCustomValidity("Passwords must be the same");

        }else{
            passwordRepeat.setCustomValidity("");
        }
    });

    form.addEventListener('submit', function(event){
        if(form.checkValidity() == false){
            event.preventDefault();
            event.stopPropagation();
        }
        else{
            form.classList.add('was-validated');
        }
    }, false);
}, false);