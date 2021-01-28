<?php

session_start();

$con = mysqli_connect('localhost','root',' ');

mysqli_select_db($con, 'userregistration');


$mail = $_POST['email'];
$pass1 = $_POST['password_1'];
$pass2 = $_POST['password_2'];

$s = "select * from usertable1 where name = '$mail' && password_1 = '$pass1' && password_2 = '$pass2'";

$result = mysqli_query($con, $s);

$num = mysqli_num_rows($result);

if($num == 1) {
    header('location:home.html');
}else{
    header('location:login.php');
}