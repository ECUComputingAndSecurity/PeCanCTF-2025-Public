# Request Header Manipulation

In this challenge you are given a link to go to, as a website, it looks like this:
![image](https://github.com/user-attachments/assets/139f731b-6c1e-4e5d-81f2-89988500c285)

Note: The IP will be different, from what you see

With a name like `Request Header Manipulation`, in a http/s site, it is likely that what the browser, is refering to are the request headers sent in all get requests.

So, you go to `Burp` and open up the website in the proxy, before moving that into the `Repeater`.
![image](https://github.com/user-attachments/assets/6c21033c-d953-4618-b46e-107e4e78072c)

The hint for this is that you need to use the `Cheese` browser, that likely refers to the `User-Agent` request header, so changing it:
```
GET / HTTP/1.1
Host: localhost:8000
Cache-Control: max-age=0
sec-ch-ua: "Not:A-Brand";v="24", "Chromium";v="134"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Linux"
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Cheese
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
```

Note: This doesn't seem to get a reply from the server at all, but if there are two empty lines afterwards, then everything is fine?

Gets the reply:
![image](https://github.com/user-attachments/assets/6afd78ec-4b09-4352-af34-276d83108bf9)

The next hint for accepting a language, likely refers to `Accepted-Language`:
```
GET / HTTP/1.1
Host: localhost:8000
Cache-Control: max-age=0
sec-ch-ua: "Not:A-Brand";v="24", "Chromium";v="134"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Linux"
Accept-Language: 1337
Upgrade-Insecure-Requests: 1
User-Agent: Cheese
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
```

This gets the reply:
![image](https://github.com/user-attachments/assets/eed77140-4450-4ada-bce1-028e31737cb4)

The next hint for accepting `flag` instead of `text/html`, that likely refers to `Accept`:
```
GET / HTTP/1.1
Host: 127.0.0.1:8000
Cache-Control: max-age=0
sec-ch-ua: "Not:A-Brand";v="24", "Chromium";v="134"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Linux"
Accept-Language: 1337
Upgrade-Insecure-Requests: 1
User-Agent: Cheese
Accept: flag
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
```

This gets the reply:
![image](https://github.com/user-attachments/assets/4fb8651c-f6b6-44b8-8318-8edde5f7a188)

The hint for sending the request at the `Unix Epoch`, likely refers to `Date`:
```
GET / HTTP/1.1
Host: 127.0.0.1:8000
Cache-Control: max-age=0
sec-ch-ua: "Not:A-Brand";v="24", "Chromium";v="134"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Linux"
Accept-Language: 1337
Upgrade-Insecure-Requests: 1
User-Agent: Cheese
Date: Thu, 01 Jan 1970 00:00:00 GMT
Accept: flag
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
```

This gets the reply:
![image](https://github.com/user-attachments/assets/ae84ad2d-f261-4960-8f32-24dc16aa6a9e)

The hint to `rickroll yourself` and then come back likely refers to either `Referer`, or `Origin`:
Lets try `Referer`, the link for rick rolling is `https://www.youtube.com/watch?v=dQw4w9WgXcQ`:
```
GET / HTTP/1.1
Host: 127.0.0.1:8000
Cache-Control: max-age=0
sec-ch-ua: "Not:A-Brand";v="24", "Chromium";v="134"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Linux"
Accept-Language: 1337
Upgrade-Insecure-Requests: 1
User-Agent: Cheese
Date: Thu, 01 Jan 1970 00:00:00 GMT
Accept: flag
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

That works, getting the reply:
![image](https://github.com/user-attachments/assets/907c62aa-67fb-4e1e-9f53-d7ee11ff4193)

The hint of using an `Effective connection`, likely refers to `Effective Connection Type` or `ECT`:
```
GET / HTTP/1.1
Host: 127.0.0.1:8000
Cache-Control: max-age=0
sec-ch-ua: "Not:A-Brand";v="24", "Chromium";v="134"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Linux"
Accept-Language: 1337
Upgrade-Insecure-Requests: 1
User-Agent: Cheese
Date: Thu, 01 Jan 1970 00:00:00 GMT
Accept: flag
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: https://www.youtube.com/watch?v=dQw4w9WgXcQ
ECT: 5g
```

This gets the reply:
![image](https://github.com/user-attachments/assets/84f4717b-bb97-456c-8991-197994725b7e)

This hint of supplying an `Email` likely refers to the `From` header, where you can give the server an email in. There isn't a hint about what email to use, so I just made one up:
```
GET / HTTP/1.1
Host: 127.0.0.1:8000
Cache-Control: max-age=0
sec-ch-ua: "Not:A-Brand";v="24", "Chromium";v="134"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Linux"
Accept-Language: 1337
Upgrade-Insecure-Requests: 1
User-Agent: Cheese
Date: Thu, 01 Jan 1970 00:00:00 GMT
Accept: flag
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: https://www.youtube.com/watch?v=dQw4w9WgXcQ
ECT: 5g
From: picklerick@example.com
```

This replies with the flag:
`pecan{HTTP_r3q35st_h34d3r5_c4n_g3t_qu1t3_w13rd_4nd_5p3c1f1c}`
