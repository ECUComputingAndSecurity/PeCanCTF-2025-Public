/*
    !TODO : This is only for testing purposes while developing the admin panel, please remember to delete it 
    once this product is deployed for everyone to use. It can be dangerous if someone forgets to delete it
    in production.
*/

// >>> Purpose: Testing out brute force attack against the login panel
// NOTE: brute forcing is not the way while doing PECAN+
var dummy_data = {
    /*
        Making 50 invalid requests to see if the login prompt is still reactively afterward..
    */
    "skywalker32": "Lx#8gR7zqP",
    "byteflux88": "T2@vM9pKtQ",
    "nighthawk47": "Wj!5dZ0uNs",
    "photonblade": "Uz$3rDf1Lp",
    "echozulu21": "Kw*7nYc4Vm",
    "cryptosniper": "Ht#6xBe8Rj",
    "vortexalpha": "Jm!9sLp3Xy",
    "silentnova": "Gn$5kQz2Wu",
    "ironcomet42": "Pb@8dNc7Vb",
    "quantumfox": "Lr!2vKm5Ty",
    "bitfalcon55": "Yx@4tGh9Nc",
    "cobaltshade": "Nm#3jWp7Zt",
    "flareion89": "Zd!6uTy1Xc",
    "ghoststrike": "Tr$9eMz4Qv",
    "frostecho13": "Qw#7pLn3Ru",
    "axionprime": "Vu@1dFg5Yz",
    "zephyrbolt": "Mx!4sJh8Vc",
    "blazebane": "Ct$6qXp2Mw",
    "darknova10": "Hs@7mVz5Rj",
    "codezenith": "Lp#9bTy1Xo",
    "stormbyte91": "Wd!3tLk8Qp",
    "lunarforge": "Jr$5nYp2Xz",
    "nebularise": "Ut@8cGw4Rm",
    "glitchraven": "Xk#2dNz7Vb",
    "novaecho20": "Qm!6yFr3Wp",
    "xenonshade": "Rg$7bTz9Lu",
    "firestrike9": "Kc@4nLw1Xt",
    "orbitghost": "Zx#5tRp6Mj",
    "aetherflare": "Ln!3mFy8Vu",
    "cyberhowl": "Bp$9xQw2Tk",
    "pixelglitch": "Yf@1zKr5Xv",
    "bluestatic": "Wq#7vTm3Nz",
    "gammahawk": "Np!6eLd4Rx",
    "vaporvortex": "Lk$2tYp7Mw",
    "onyxember": "Jz@5rWn8Vu",
    "thunderhex": "Mx#8bTy1Pq",
    "silentradar": "Ks!9tPw3Nv",
    "ravenstrike": "Gn$3xJk7Wz",
    "pulseflare": "Uy@6qZn2Tv",
    "mechablade": "Wc#1vGy9Lp",
    "nexusglide": "Jr!8nLp3Rx",
    "quantadash": "Tb$4zPk5Mw",
    "fusionnova": "Xp@3tYq7Rv",
    "zetaecho32": "Ln#6mWp1Vb",
    "driftzebra": "Yx!7cFt8Np",
    "bioflame77": "Qr$5kNz2Mw",
    "neonmirage": "Tc@8pGw4Xy",
    "cybertrail": "Kv#9rLp1Vu",
    "zenoraptor": "Wm!2dFy7Tq",
    "cloudburn": "Zt$3xNk8Lv",
    "hexnova77": "Jx@6mLp4Vq"
}

function brute_force() {

    // Call to brute force 

    for (let [user, passwd] of Object.entries(dummy_data)) {
        $.post("/admin/challenges/dashboard", {
            password: passwd,
            username: user
        }, function (data, status) {
            console.log(`>> Bf attempt => ${user}:${passwd}`);
        });
    }

}

const verify_ = () => { // Call GuardDuty of CWS ( CodeCTF Web Services :D ) to make sure the brute force was stopped.
    $.ajax({
        // url: "/v1/api/admin/guarddefense/shield/status",
        // ^^^ Not working, had to check /v1/api/admin/swagger.json to make sure I got the right path
        // and i think the following might be right instead ? idk

        url: "/v1/api/admin/guardduty/status",
        headers: { "Authorization": "Bearer SUp3Rs3cReTAPI_k3y--f0r-_c0deCtFAdMiN" }, // HHmmm 🧐
        success: (e) => {
            if (e.status === "BLOCKED")
                alert("IT WORKED !!!!")
        }
    })
}

// Sorry, i'm bored during development sometime.
const I_have_no_idea_why_i_declared_this_variable = "https://youtu.be/dQw4w9WgXcQ"