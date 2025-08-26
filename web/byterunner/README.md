# ByteRunner Delivery Services

## Overview

This challenge is actually based on a real-world vulnerability that I encountered by accident in my own home infrastructure.
It's super easy to accidentally leave open, and if you know how to exploit it, can be pretty dangerous.

The core of the challenge is to exploit a common problem in reverse proxy setups, which are common in many web applications.

## Hints

1. Most reverse proxies will serve multiple sites or services. How do they know which one to serve?
2. Have a look at the HTTP traffic between your browser and the server. What information is being sent that could help the proxy decide which site to serve?
3. Have a look at the `Host` header in the HTTP request. What does it do?
4. Can you manipulate the `Host` header to make the server serve a different site or service?

## Solution

If you have a look at the website source briefly, you'll notice that on the support page, there's commented out code that contains a link to "http://intranet.byterunner".

This is obviously not a real domain as `byterunner` is not a valid TLD, which is a hint that it's probably some private/internal domain that the company uses within their network.

Lots of companies use internal domains like this to access their internal services, as devices on their network will usually use the company's DNS servers, so you aren't restricted to publicly available domains.

This server is on a reverse proxy that also serves the public website, which is also a common setup for many companies that allows serving multiple sites or services from a single IP address.

The reverse proxy uses the `Host` header in the HTTP request to determine which site or service to serve.

In our case, the reverse proxy is configured to serve the public website unless the `Host` header is set to `intranet.byterunner`, in which case it will serve the internal site instead.

To exploit this, we can use a tool like `curl` to send a request to the server with the `Host` header set to `intranet.byterunner`.

```bash
curl -H "Host: intranet.byterunner" http://localhost:8080/ # Except instead of localhost:8080 you'd reference the actual challenge URL
```

Alternatively, you can use a browser extension like [ModHeader](https://modheader.com/) to modify the `Host` header in your browser.

Either way, this will cause the reverse proxy to serve the internal site instead of the public site.

Once you get to the internal site, you'll be able to see the flag!
