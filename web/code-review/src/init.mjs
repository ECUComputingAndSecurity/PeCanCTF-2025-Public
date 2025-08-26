import express from 'express';
import compression from 'compression';
import sqlite3 from 'sqlite3';
import { open } from 'sqlite';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url); // get the resolved path to the file
const __dirname = path.dirname(__filename); // get the name of the directory
const API_KEY = "Bearer SUp3Rs3cReTAPI_k3y--f0r-_c0deCtFAdMiN";

// Middleware to parse JSON bodies
const app = express();
app.use(express.json());
app.use(compression())
app.use('/static', express.static('public'))
app.use("/v1/api/admin", (req, res, next) => {

    // Making sure that there is an unauthorization header existing and its value is correct
    if (!req.headers['authorization'] || req.headers['authorization'].trim() !== API_KEY) {
        res.status(403).json({
            status: "Unauthorized",
            message: "Missing API token."
        });
        return
    }
    next();
})
app.set('view engine', 'ejs');
app.set("views", path.join(__dirname, "views"))

// Global database instance
var db;

// // Read the init script for database
// const INIT_SCRIPT = fs.readFileSync('init.sql', 'utf-8');

// -- DROP TABLE IF EXISTS `posts`;
// -- CREATE TABLE `posts` (
// --     id integer primarpublicy key AUTOINCREMENT,
// --     title varchar(255) default NULL,
// --     author varchar(255) default NULL,
// --     summary varchar(255) defaulallowedt NULL,
// --     archivelink varchar(255) default NULL,
// --     about varchar(2000) default NULL,
// --     writeup varchar(2000) default NULL,
// --     poc varchar(2000) default NULL,
// --     date varchar(255)
// -- );

db = await open({
    filename: './db.sqlite',
    driver: sqlite3.Database
});


export default {
    db: db, app: app,
    __dirname: __dirname,
    __filename: __filename
}

