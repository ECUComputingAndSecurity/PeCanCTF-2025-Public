function alert_success() {
    $('.toast-container').append(`
    <div class="toast success-toast" role="alert" aria-live="assertive" aria-atomic="true">
        <div class="toast-header text-bg-primary">
        <img src="/static/imgs/flag.png" height="20em" width="20em" class="rounded me-2" alt="...">
        <strong class="me-auto">Success</strong>
        <small>Now</small>
        <button type="button" class="btn-close" data-bs-dismiss="toast"></button>
        </div>
        <div class="toast-body text-bg-primary">
        Your challenge has been successfully uploaded. Please wait for the administrators to review then an email will
        be sent directly to your inbox or if you are one, click <a href="/admin/challenges/dashboard">here</a> to review the challenges.
        </div>
    </div>`)
    bootstrap.Toast.getOrCreateInstance($('.toast-container > div:last-child')).show()
}

function alert_error(msg) {
    $('.toast-container').append(`
    <div class="error-toast toast" role="alert" aria-live="assertive" aria-atomic="true">
        <div class="toast-header text-bg-danger">
        <img src="/static/imgs/flag.png" height="20em" width="20em" class="rounded me-2" alt="...">
        <strong class="me-auto">Error</strong>
        <small>Now</small>
        <button type="button" class="btn-close" data-bs-dismiss="toast"></button>
        </div>
        <div class="toast-body text-bg-danger">
        ${msg}
        </div>
    </div>`)
    bootstrap.Toast.getOrCreateInstance($('.toast-container > div:last-child')).show()
}



$('.dragdrop').on("dragover", (e) => {
    $('.dragdrop').addClass("dragdrop-hovered")
})
$('.dragdrop').on("dragleave", (e) => {
    $('.dragdrop').removeClass("dragdrop-hovered")
})

$(".dragdrop").on("click", (e) => {
    $('input[name="filechal"]').click();
})

$('input[name="filechal"]').on('change', (e) => {
    $(".dragdrop").addClass("dropped");

    // This is actually self-XSS, don't do this in real life coding.
    // But it's just a fact, it's not gonna be the key to solving this
    // challenge, lol.
    $("#upload-file-section").html(e.target.files[0].name);

    upload_file(e.target.files[0])
})

$(".submitbtn").on("click", (e) => {
    $(".c-modal").addClass("show")
})

$("#cancel").on("click", () => {
    $(".c-modal").removeClass("show")
})

var file = null;

const upload_file = (f) => file = f;

const upload_challenge = () => {
    // make a request to the API to submit the challenge

    // This is actually another LOW/INFO severity vuln, which is Improper Input Validation or Excessive trust on the Frontend ;)
    // Notice how it doesn't verify whether the email is correct and whether the actual metadata and filetype of the uploaded 
    // file ? Again, just an insight, it's not gonna be the key toward solving this challenge, now have fun :D

    const email = $("input[type='email']").val().trim();
    const name = $("input[type='name']").val().trim();

    // checkboxes
    const category = $("input[name='inlineRadioOptions']:checked");

    if (email === '')
        alert_error("Missing 'email' field in the form.")
    else if (name === '')
        alert_error("Missing author's name in the form.")
    else if (category.length === 0)
        alert_error("Please choose a category.")
    else if (file === null)
        alert_error("Missing challenge's source code.")
    else {

        // Start uploading the challenge here
        $('#send_challenge > label').css("display", "none");
        $('#send_challenge > div.spinner-border').removeClass("hide");

        const form = new FormData();
        form.append('email', email);
        form.append('name', name);
        form.append('category', category);
        form.append('file', file);

        fetch("/v1/api/challenge/submit", {
            method: "POST",
            body: form
        })
            .then(res => res.json())
            .then(data => {
                $('#send_challenge > label').css("display", "block");
                $('#send_challenge > div.spinner-border').addClass("hide");
                $(".c-modal").removeClass("show")
                alert_success()
            }).catch(e => {
                $('#send_challenge > label').css("display", "block");
                $('#send_challenge > div.spinner-border').addClass("hide");
                alert_error(console.error(e.message))
            })

    }

}

$("#send_challenge").on("click", () => {
    upload_challenge();
})

$('.dragdrop').bind('dragover drop', function (event) {
    event.stopPropagation();
    event.preventDefault();
    if (event.type == 'drop') {

        $(".dragdrop").addClass("dropped");


        const file = event.originalEvent.dataTransfer.files[0];

        $("#upload-file-section").html(file.name);

        upload_file(file)

    }
});

const formatDate = (secs) => {
    const hours = Math.floor(secs / 3600); // Getting current hours
    const minutes = Math.floor((secs - (3600 * hours)) / 60) // Getting current minutes
    const seconds = secs - (minutes * 60 + 3600 * hours) // Getting seconds
    return {
        sec: `${seconds}`.padStart(2, "0"),
        hour: `${hours}`.padStart(2, "0"),
        min: `${minutes}`.padStart(2, "0")
    }
}
var timeleft = 86400;

$("#hour").html = 22;

fetch("/v1/api/timeleft").then(r => r.json()).then(resp => {
    timeleft = resp.time
    let t = formatDate(timeleft)

    $("#hour").text(t.hour);
    $("#min").text(t.min);
    $("#sec").text(t.sec);
})
setInterval(() => {
    let t = formatDate(timeleft)

    $("#hour").text(t.hour);
    $("#min").text(t.min);
    $("#sec").text(t.sec);

    timeleft -= 1;
}, 1000)