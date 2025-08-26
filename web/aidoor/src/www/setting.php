<?php

$database_file = realpath(dirname(__FILE__)) . '/database.db';
$db = new SQLite3($database_file);

?>