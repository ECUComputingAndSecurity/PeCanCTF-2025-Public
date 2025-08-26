import singleton from './init.mjs';
import swaggerJSDoc from 'swagger-jsdoc';
import path from 'path'
import fs from 'fs';
import { dir } from 'console';

const app = singleton.app;
const dirname = singleton.__dirname;
var timeleft = 86400;
// 86400 seconds = 1 day, this is for /timeleft endpoint which tell the frontend UI how much time is left 
// before the last wave of submission ends.

const swaggerDefinition = {
    openapi: '3.0.0',
    info: {
        title: 'CodeCTF Web Services - CWS Administrator Endpoints',
        version: '1.0.0',
        description: 'API docs',
    },
    paths: {
        "/v1/api/admin/swagger.json": {
            method: "GET",
            "description": "Showing all available endpoints.",
            "parameters": null
        },
        "/v1/api/admin/secret-manager/list": {
            method: "GET",
            "description": "List all available secrets/passphrases.",
            "parameters": null
        },
        "/v1/api/admin/secret-manager/get": {
            method: "GET",
            "description": "Extract a certain secret/passphrase.",
            "parameters": {
                "id": "ID of the secret."
            }
        },
        "/v1/api/admin/bucket/list": {
            method: "GET",
            "description": "List all available buckets.",
            "parameters": null
        },
        "/v1/api/admin/bucket/get": {
            method: "GET",
            "description": "Extract a certain bucket.",
            "parameters": {
                "id": "ID of the bucket."
            }
        },
        "/v1/api/admin/guardduty/status": {
            method: "GET",
            "description": "Threat and brute forcing detection ( Not working rn ! ).",
            "parameters": null
        },
    }
};

const options = {
    swaggerDefinition,
    apis: ['./routes/*.js'], // Your route files
};
const swaggerSpec = swaggerJSDoc(options);
// ---- Administrators API definitions

const SECRETS = JSON.parse(fs.readFileSync(path.join(dirname, "secrets", "all_secrets.json"), "utf8"));
const BUCKETS = JSON.parse(fs.readFileSync(path.join(dirname, "bucket", "buckets.json"), "utf8"));

app.get('/v1/api/admin/swagger.json', (req, res) => {
    res.setHeader('Content-Type', 'application/json');
    res.send(swaggerSpec);
})
app.get("/v1/api/admin/secret-manager/list", (req, res) => {
    res.json({ secrets: SECRETS.secrets });
})
app.get("/v1/api/admin/secret-manager/get", (req, res) => {

    if (!req.query.id) {
        res.status(400).json({
            message: "Missing parameter 'id'"
        })
        return
    }

    if (!SECRETS.mapping.hasOwnProperty(req.query.id)) {
        res.status(400).json({
            message: `Unable to find any bucket with the id of '${req.query.id}'`
        })
        return
    }

    res.json({
        status: "Found",
        key: SECRETS.mapping[req.query.id]
    })
})
app.get("/v1/api/admin/bucket/list", (req, res) => {
    res.json({ buckets: BUCKETS.buckets })
})
app.get("/v1/api/admin/bucket/get", (req, res) => {

    if (!req.query.id) {
        res.status(400).json({
            message: "Missing parameter 'id'"
        })
        return
    }

    if (!BUCKETS.mapping.hasOwnProperty(req.query.id)) {
        res.status(400).json({
            message: `Unable to find any bucket with the id of '${req.query.id}'`
        })
        return
    }

    // Download the file
    res.download(path.join(dirname, "bucket", BUCKETS.mapping[req.query.id]));
})
app.get("/v1/api/admin/guardduty/status", (req, res) => {
    // Making sure the user is safe and no brute forcing attempt was made
    const ip = req.headers['x-forwarded-for'] ? req.headers['x-forwarded-for'] : req.connection.remoteAddress;
    res.json({
        ip: ip,
        status: "Processing"
    });
})

// ---- How much time left before the submission portal closes.
setInterval(() => timeleft -= 1, 1000)
app.get("/v1/api/timeleft", (req, res) => {
    res.json({ time: timeleft })
})
app.post("/v1/api/challenge/submit", (req, res) => {
    res.json({
        status: "Success"
    });
})