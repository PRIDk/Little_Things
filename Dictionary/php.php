<?php

$serverName = "localhost";
$userName = "root";
$password = "";
$dbname = "test";

// connection

$connection = mysqli_connect($serverName, $userName, $password, $dbname);

if(mysqli_connect_errno()) {
    echo "Failed to connect!"
    exit;
}
echo "Connection success!";


?>