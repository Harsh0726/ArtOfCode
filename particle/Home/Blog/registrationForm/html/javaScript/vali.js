function validation() {
    var userName = document.forms["RegForm"]["name"];
    var mail = document.forms["RegForm"]["email"];
    var userPassword = document.forms["RegForm"]["password_1"];
    var confirmPassword = document.forms["RegForm"]["password_2"];
 
    if (userName.value == "") {
        window.alert("Please enter your name.");
        userName.focus();
        return false;
    }

    if (mail.value == "") {
        window.alert("Please enter your e-mail address");
        mail.focus();
        return false;
    }

    if (userPassword.value == "") {
        window.alert("Please enter your password.");
        userPassword.focus();
        return false;
    }

    if (confirmPassword.value == "") {
        window.alert("Please re-enter your password.");
        confirmPassword.focus();
        return false;
    }

    return true;
}