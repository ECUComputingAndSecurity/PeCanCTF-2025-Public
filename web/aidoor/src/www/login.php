<?php
session_start();
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AiDoor - Login</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@1.0.2/css/bulma.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css"
        integrity="sha512-Evv84Mr4kqVGRNSgIGL/F/aIDqQb7xQ2vcrdIwxfjThSH8CSR7PBEakCr51Ck+w+/U6swU2Im1vVX0SVk9ABhg=="
        crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link href="css/register.css" rel="stylesheet" />
    <link rel="icon" type="image/x-icon" href="/images/door.png">
</head>

<body>

    <?php

    include 'setting.php';

    $_ok = "";
    $_err = "";

    if (isset($_GET['new']) && $_GET['new'] == 1) {
        $_ok = 'Registration succeeded, now try to login.';
        $_err = "";
    }

    if (isset($_POST['username'])) {

        $username = $_POST['username'];
        
        $stmt = $db->prepare('SELECT * FROM users WHERE username=:username');
        $stmt->bindValue(':username',$username, SQLITE3_TEXT);
        $result = $stmt->execute();

        if (!$result->fetchArray()) {
            $_err = "Account with username '" . $username . "' does not exist.";
            $_ok = "";
        } else {

            // new result again
            $password = $_POST['password'];

            $stmt = $db->prepare('SELECT * FROM users WHERE username = :username AND password = :password');
            $stmt->bindValue(':username',$username, SQLITE3_TEXT);
            $stmt->bindValue(':password',$password, SQLITE3_TEXT);
            $result = $stmt->execute();

            $row = $result->fetchArray(SQLITE3_ASSOC);

            if (!$row) {
                $_err = "Invalid password.";
                $_ok = "";
            } else {
                $_ok = "";
                session_regenerate_id(true);
                $_SESSION['authid'] = $row['id'];
                $_SESSION['authname'] = $row['username'];
                header("Location: /");
                die();
            }
        }

    }
    ?>

    <div id="main">
        <form action="" method="POST">
            <h1 class="title has-text-link">Login</h1>
            <div class="field">
                <label class="label">Username</label>
                <div class="control has-icons-right">
                    <input class="input" name="username" type="text" placeholder="Username">
                </div>
            </div>
            <div class="field">
                <label class="label">Password</label>
                <div class="control has-icons-right">
                    <input class="input" name="password" type="password" placeholder="Password">
                </div>
            </div>

            <h6 class="is-6 has-text-danger error"><?php echo $_err ?></h6>
            <h6 class="is-6 has-text-success ok"><?php echo $_ok; ?></h6>

            <div class="field mt-5 is-grouped">
                <button type="submit" class="button is-link ">Login</button>
            </div>
            <h6 class="is-6 is-link">New to the site ? Register <a href="/register.php">here</a>.</h6>

        </form>
    </div>
</body>
<script src="https://code.jquery.com/jquery-1.9.1.js"></script>
<script>

    $("form").on('submit', (e) => {
        e.preventDefault();

        const passwd = $('input[name="password"]');
        const username = $('input[name="username"]');
        const pass = passwd.val().trim();
        const un = username.val().trim();

        passwd.removeClass("is-danger");
        username.removeClass("is-danger");

        if (un === '') {
            username.addClass("is-danger");
            $(".error").html("Please provide a username.");
            return;
        }
        if (pass === '') {
            passwd.addClass("is-danger");
            $(".error").html("Please provide a password.");
            return;
        }

        e.target.submit();
    })

</script>

</html>