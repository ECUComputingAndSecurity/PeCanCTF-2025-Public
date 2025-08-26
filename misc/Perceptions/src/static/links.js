const LINKS = {
    "Welcome!":            "25YDY4737K3QMIZ6N5OUEYGL",
    "My Server":           "6PP5RVOYV54Z7DUASYLKF2FK",
    "What I'm Working On": "3XSPO7ZJP27IUGMANNB2V2J3",
    "Holday":              "MHEGSBREXSEDFLXPWXVAA2GQ",
    "Secret Post":         "4C6Y4NEBVLATCF6EX5PA2ISZ"
};

// Fill navbar
window.onload = function() {
    fetch("/name").then((response) => {
        response.text().then((text) => {
            const name = document.getElementById("name");
            name.innerText = name.innerText.replaceAll("[placeholder]", text);
        });
    });

    let nav = document.getElementById("navlist");
    for (const [label, location] of Object.entries(LINKS)) {
        const node = document.createElement("li");
        const link = document.createElement("a");
        const text = document.createTextNode(label);
        link.href = "/" + location + "/page.html";
        link.appendChild(text);
        node.appendChild(link);
        nav.appendChild(node);
    }
    const node = document.createElement("li");
    const link = document.createElement("a");
    const text = document.createTextNode("Login (WIP)");
    link.href = "/login.html";
    link.appendChild(text);
    node.appendChild(link);
    nav.appendChild(node);
}
