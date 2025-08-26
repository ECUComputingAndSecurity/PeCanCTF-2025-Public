# Perceptions

## Flag

- `pecan{p3rsp3c71v3.15.k3y}`

## Writeup

1. Going to the website we can see that there are a few posts, 'My Server' specifically talking about this server having remote access tools and a web server, and how everything is reduced into one port
2. We can look at 'Secret Post' to see that credentials are hidden somewhere on the page. This is in a HTML comment on that same post, the credentials are `Charlie:UlLOPNeEak9rFfmL`.
3. We can try the login page, but as stated on the site this doesn't work, time to pivot.
4. Running `nmap` on the web port is an option, but service scans do not return valid results. Part of the result may be a worthwhile hint though: `"Detected\x20protocol\x20'UNKNOWN',\x20Perceptions\x20cannot\x20serve\x20this\x20protocol\.\x20Supported:\x20HTTP,\x20SSH\r\n"`. This can also be found by using `netcat` on the port and typing random input data.
5. We know we can use SSH and HTTP on the port, let's try SSH
6. We get a login prompt, so let's use the details from before
7. These work due to the website login being integrated with the system authentication, and we have a shell
8. `ls` to see files, `cat flag.txt` to show the flag

### Sidenote

The SSH server keys are fine to be there, they're only used for the challenge and was just easier to pre-generate them, plus could be useful to analyse traffic if necessary at any point
