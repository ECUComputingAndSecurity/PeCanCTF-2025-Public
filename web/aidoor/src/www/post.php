<?php

session_start();

if (!isset($_SESSION['authid'])) {
    // Have to login first
    header("Location: /login.php");
    die();
}

// Check if the id is present and if yes, is it a valid number ?
if (!isset($_GET['id']) || !is_numeric($_GET['id'])) {
    http_response_code(400);
    header('Content-Type: application/json');
    echo json_encode([
        'status' => 400,
        'message' => "Bad request, invalid 'id' parameter. make sure it's a number."
    ]);
    exit;
}


// Make sure the id isn't too big
if ($_GET['id'] > 50) {
    http_response_code(response_code: 500);
    header('Content-Type: application/json');
    echo json_encode([
        'status' => 500,
        'message' => "Nope nope, 'id' should not be bigger than 50 or smaller than 0, our application isn't scalable yet so there won't be many posts."
    ]);
    exit;
}

include 'setting.php';


$stmt = $db->prepare('SELECT * FROM posts WHERE id=:id_');
$stmt->bindValue(":id_", $_GET['id'], SQLITE3_INTEGER);
$result = $stmt->execute();
$result = $result->fetchArray();

if (!$result) {
    http_response_code(404);
    echo "No such post exist with id=" . $_GET['id'];
    exit;
}

if (isset($_GET['get_content_only']) && $_GET['get_content_only'] == 'true') {
    header('Content-Type: text/html');
    echo $result['content'];
    exit;
}

if ($result['type'] == 0) {
    // It's a draft by the administrator, just ignore it then kill the rest of the process
    http_response_code(response_code: 403);
    header('Content-Type: application/json');
    echo json_encode([
        'status' => 403,
        'message' => "This post is currently a draft, only administrators can access it."
    ]);
    exit;
}

?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AiDoor - <?php echo $result['title']; ?> </title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@1.0.2/css/bulma.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css"
        integrity="sha512-Evv84Mr4kqVGRNSgIGL/F/aIDqQb7xQ2vcrdIwxfjThSH8CSR7PBEakCr51Ck+w+/U6swU2Im1vVX0SVk9ABhg=="
        crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.8.1/github-markdown.min.css"
        integrity="sha512-BrOPA520KmDMqieeM7XFe6a3u3Sb3F1JBaQnrIAmWg3EYrciJ+Qqe6ZcKCdfPv26rGcgTrJnZ/IdQEct8h3Zhw=="
        crossorigin="anonymous" referrerpolicy="no-referrer" />

    <link href="css/post.css" rel="stylesheet" />
    <link rel="icon" type="image/x-icon" href="/images/door.png">
</head>
<script src="https://cdn.jsdelivr.net/npm/markdown-it@14.1.0/dist/markdown-it.min.js"
    integrity="sha256-OMcKHnypGrQOLZ5uYBKYUacX7Rx9Ssu91Bv5UDeRz2g=" crossorigin="anonymous"></script>

<body>
    <nav class="navbar" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">
            <a class="navbar-item" href="#" onclick="history.back()">
                <i class="fa-solid fa-chevron-left"></i>
            </a>
        </div>
        <div class="navbar-brand">
            <a class="navbar-item" href="/">
                <img src="/images/door.png" />
                <h3 class="is-1">AiDoor's Blog</h3>
            </a>
        </div>

        <div id="title_" class="navbar-menu">
            <div class="navbar-end">
                <h1 class="title is-6"><?php echo $result['title']; ?></h1>
            </div>
        </div>
    </nav>

    <article id="main" class="markdown-body">
    </article>
</body>
<script src="https://code.jquery.com/jquery-1.9.1.js"></script>

<script>


    const id_ = (new URLSearchParams(window.location.search)).get("id");

    fetch(`/post.php?id=${id_}&get_content_only=true`).then(e => e.text()).then(response => {
        const md = window.markdownit();
        const result = md.render(response.trim());
        $("#main").html(result);
    })


</script>


</html>