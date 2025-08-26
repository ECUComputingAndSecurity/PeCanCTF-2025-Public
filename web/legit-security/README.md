# Legit Security Website

## Flag

- `pecan{d0nt_Bl1ndly_tru$t_everyth1ng:(}`

## Writeup

1. **Explore the Portal**
   - Open the site and notice the prominent "Admin Dashboard" button. Naturally, you click it.
2. **Infinite Redirect**
   - You are stuck in an infinite redirect loop and can't access the admin page. Frustrated, you go back.
3. **Clues About Middleware**
   - The homepage and code mention "Next.js middleware". You research and find a recent exploit involving special headers.
4. **Research the Exploit**
   - You find a GitHub advisory about bypassing Next.js middleware using the `x-middleware-subrequest` header.
5. **Craft a Bypass Request**
   - In Chrome DevTools, you copy the infinite redirect request as fetch, add the `x-middleware-subrequest` header, and send it in the console.
6. **Find the Secret Admin URL**
   - The network response now contains HTML with a secret code, e.g. `<code>/admin/9b80b2ab-fde1-4ea4-b7bc-3c8f4e20847c</code>`.
7. **Access Phase 2**
   - You visit this secret URL and reach the final phase page.
8. **Try the Button**
   - You click the big button to claim your reward, but get an error message.
9. **Inspect the Request**
   - In DevTools, you see the request body is `[{"isCompleted":false}]`. You resend the request, changing `isCompleted` to `true`.
10. **Claim the Token**
    - The server responds with `{"success":true,"token":"pecan{d0nt_Bl1ndly_tru$t_everyth1ng:(}"}`. You have solved the challenge!
