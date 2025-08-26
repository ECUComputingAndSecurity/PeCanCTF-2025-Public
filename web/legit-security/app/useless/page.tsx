export default function UselessPage() {
    const facts = [
        "Our admin dashboard is protected by state-of-the-art Next.js middleware...",
        "You can use Chrome DevTools to right-click a network request and 'Copy as fetch' to replay or modify it...",
        "We believe in transparency. Check our /robots.txt for our crawling policy.",
        "The HTTP 418 status code means 'I'm a teapot'.",
        "Security.txt is a new industry standard for vulnerability disclosure.",
        "The X-Frame-Options header can prevent clickjacking.",
        "The SameSite cookie attribute helps prevent CSRF attacks.",
        "CSP (Content Security Policy) can help mitigate XSS.",
        "The favicon.ico file is requested by browsers automatically.",
        "The Accept-Language header can be used for localization.",
        "The X-Powered-By header can leak tech stack info.",
        "The HTTP 451 status code means 'Unavailable For Legal Reasons'.",
        "The HTTP 204 status code means 'No Content'.",
        "The HTTP 200 status code means 'OK'.",
        "The HTTP 404 status code means 'Not Found'.",
        "The HTTP 500 status code means 'Internal Server Error'.",
        "The HTTP 302 status code means 'Found' (redirect).",
        "The HTTP 307 status code means 'Temporary Redirect'.",
        "The HTTP 308 status code means 'Permanent Redirect'.",
        "The HTTP 401 status code means 'Unauthorized'.",
        "The HTTP 403 status code means 'Forbidden'.",
        "The HTTP 400 status code means 'Bad Request'.",
        "The HTTP 301 status code means 'Moved Permanently'.",
        "The HTTP 202 status code means 'Accepted'.",
        "The HTTP 206 status code means 'Partial Content'.",
        "The HTTP 100 status code means 'Continue'.",
        "Our knowledge base is always growing. Check back for more tips!",
        "You can use the Fetch API in JavaScript to make HTTP requests.",
        "The Referrer-Policy header controls what referrer info is sent.",
        "The XSS Auditor is deprecated in modern browsers.",
        "The /etc/passwd file is not accessible from the browser. Usually.",
        "The Set-Cookie header can set multiple cookies at once.",
        "The HTTP TRACE method is rarely enabled for a reason.",
        "The admin password is not 'admin'!",
        "The Content-Type header tells browsers how to interpret content.",
        "The HTTP OPTIONS method can reveal allowed methods.",
        "The Knowledge Base is for informational purposes only.",
        "The robots meta tag can also control indexing.",
        "Some CTFs hide clues in HTTP response headers.",
        "The /admin page is totally secure. Trust us...",
        "The first computer virus was called Creeper and appeared in the early 1970s.",
        "The first web server was Tim Berners-Lee's NeXT computer.",
        "Browsers ignore unknown HTTP headers.",
        "You can use the 'view-source:' prefix in browsers to see raw HTML.",
        "The flag is never in the source code. Or is it?",
        "The /useless page is truly useless.",
        "The /.well-known/security.txt file might exist. Or not...",
        "The admin page is not in /robots.txt. Or is it?",
        "Our support team is always here to help (not really).",
        "Security is a journey, not a destination.",
        "Thank you for using Legit Security Portal!"
    ].sort(() => Math.random() - 0.5);
    return (
        <div className="flex flex-col items-center justify-center min-h-screen p-3 bg-gradient-to-br from-gray-950 via-blue-950 to-purple-950 dark:from-gray-900 dark:via-blue-900 dark:to-purple-900 rounded-md ">
            <div className="bg-white/10 dark:bg-gray-900/70 backdrop-blur-md rounded-2xl shadow-2xl p-10 max-w-3xl w-full text-center border border-blue-700 dark:border-blue-800 h-full">
                <h2 className="text-4xl font-extrabold mb-4 text-blue-200 dark:text-blue-300 drop-shadow">Knowledge Base</h2>
                <p className="mb-8 text-lg text-gray-200 dark:text-gray-300">
                    Welcome to the Legit Security Knowledge Base. Here you'll find a curated collection of security facts, tips, and trivia from our team.
                </p>
                <ul className="mb-8 text-left text-gray-300 dark:text-gray-400 list-disc list-inside max-h-[32rem] overflow-y-auto grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-2 px-2">
                    {facts.map((fact, i) => (
                        <li key={i} className="mb-2 text-base leading-relaxed">{fact}</li>
                    ))}
                </ul>
                <div className="mt-6 text-gray-400 dark:text-gray-500 text-sm italic">
                    Have a tip to share? Contact our (fictional) support team!
                </div>
            </div>
        </div>
    );
}

export const metadata = {
    title: "Legit Security Knowledge Base | Many of the things listed here are important...",
}
