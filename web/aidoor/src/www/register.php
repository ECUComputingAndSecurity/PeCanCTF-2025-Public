<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AiDoor - Register</title>
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

    $username = $_POST['username'];
    $password = $_POST['passwd'];

    $error_ = "";
    $name_taken = false;

    // $stmt = $db->prepare('SELECT * FROM users WHERE username=:username');
    // $stmt->bindValue(":username", $username, SQLITE3_TEXT);
    // $result = $stmt->execute();

    // if ($result->fetchArray(1)) {
    // // user with this name has already existed, better off switch to another
    //     $error_ = "'" . $username . "' is already taken.";
    //     $name_taken = true;
    // } else 
    
    if (isset($_POST['username']) && isset($_POST['passwd'])) {
        // Insert a new record

        $stmt_insert = $db->prepare('INSERT INTO users(username,password) VALUES(:username, :passwd)');
        $stmt_insert->bindValue(':username', $username, SQLITE3_TEXT);
        $stmt_insert->bindValue(':passwd', $password, SQLITE3_TEXT);
        $result = $stmt_insert->execute();

        if($db->lastErrorCode() == 0){
            header("Location: /login.php?new=1");
            die();    
        }else{
            $name_taken = true;
            $error_ = $db->lastErrorCode()==19 ? "'" . $username . "' is already taken." : "An unexpected error occurred. Please try again.";
        }
    }

    ?>

    <div id="main">
        <form action="" method="POST">
            <h1 class="title has-text-link">Join now!</h1>
            <h6 class="subtitle is-6 mt-2 mb-5">Register now to become a member.</h6>
            <div class="field">
                <label class="label">Username</label>
                <div class="control has-icons-right">
                    <input class="input <?php echo $name_taken ? 'is-danger' : '' ?>" name="username" type="text"
                        placeholder="Username">
                </div>
            </div>
            <div class="field">
                <label class="label">Password</label>
                <div class="control has-icons-right">
                    <input class="input" name="passwd" type="password" placeholder="Your Password">
                    <input class="input mt-3" name="cpasswd" type="password" placeholder="Confirm Password">
                </div>
            </div>

            <h6 class="is-6 text-err has-text-danger"><?php echo $error_ ?></h6>

            <div class="field mt-5 is-grouped">
                <button type="submit" class="button is-link ">Register</button>
            </div>
            <h6 class="is-6 is-link">Already have an account ? Login <a href="/login.php">here</a>.</h6>

        </form>
    </div>
</body>
<script src="https://code.jquery.com/jquery-1.9.1.js"></script>

<script>

    $('form').on("submit", (e) => {
        e.preventDefault();

        const userf = $('input[name="username"]');
        const passwdf = $('input[name="passwd"]');
        const cpasswdf = $('input[name="cpasswd"]');

        passwdf.removeClass("is-danger");
        cpasswdf.removeClass("is-danger");
        userf.removeClass('is-danger');


        if (userf.val().trim() === '') {
            userf.addClass("is-danger");
            $('.text-err').html("Please provide a username.");
            return;
        }

        if (passwdf.val().trim() === '') {
            passwdf.addClass("is-danger");
            $('.text-err').html("Please provide a password.");
            return;
        }
        if (cpasswdf.val().trim() === '') {
            cpasswdf.addClass("is-danger");
            $('.text-err').html("Please confirm your password.");
            return;
        }

        if (cpasswdf.val().trim() !== passwdf.val().trim()) {
            cpasswdf.addClass("is-danger");
            passwdf.addClass("is-danger");
            $('.text-err').html("Password doesn't match.");
            return;
        }

        e.target.submit();

    })

</script>

</html>