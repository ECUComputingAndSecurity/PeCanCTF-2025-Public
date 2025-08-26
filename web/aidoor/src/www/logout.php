<?php

session_start();

if (!isset($_SESSION['authid'])) {
    header("Location: /login.php");
    die();
}

session_unset();
session_destroy();

header("Location: /login.php");
die();

?>