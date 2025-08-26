import singleton from './init.mjs';
import './api.mjs';
import markdownit from 'markdown-it'

const PORT = process.env.PORT || 3000;
const app = singleton.app;
const db = singleton.db;
const __dirname = singleton.__dirname
const __filename = singleton.__filename
const md = markdownit()

// ---- Route definitions below
app.get('/', async (req, res) => {
    // Show the front page, listing all submissions
    const rows = await db.all('SELECT * FROM posts');
    res.render('index', { rows: rows })
});

app.get('/challenge/:id', async (req, res) => {
    // Show the page of the submimages/favicon.icoission

    const data = await db.all('SELECT * FROM posts WHERE id=?', [req.params.id]);
    const about = md.render(data[0].about);
    const writeup = md.render(data[0].writeup);
    res.render("challenge", { title: data[0].title, link: data[0].archivelink, poc: data[0].poc, about: about, writeup: writeup })
})

app.post("/admin/challenges/dashboard", (req, res) => {
    res.redirect("/admin/challenges/dashboard?err=INVALID_CRED")
})

app.get("/admin/challenges/dashboard", (req, res) => {
    // Login before moving to the panel
    res.render("login")
})



app.listen(PORT, () => {
    console.log("challenge running at port 3000");
});
