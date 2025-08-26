import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import Link from "next/link";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Legit Security | Better than all banks combined!",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased bg-gradient-to-br from-gray-950 via-purple-950 to-blue-950 min-h-screen text-white`}
      >
        <div className="max-w-3xl mx-auto px-4 py-8">
          <header className="mb-8 flex flex-col items-center">
            <h1 className="text-4xl font-extrabold text-purple-300 drop-shadow mb-2 tracking-tight">
              Legit Security Portal
            </h1>
            <nav>
              <ul className="flex gap-6 text-lg font-mono">
                <li>
                  <Link className="hover:text-purple-400 transition" href="/">Home</Link>
                </li>
                <li>
                  <Link className="hover:text-blue-400 transition" href="/admin">Admin</Link>
                </li>
                <li>
                  <Link className="hover:text-yellow-400 transition" href="/useless">Knowledge Base</Link>
                </li>
              </ul>
            </nav>
          </header>
          <main className="mb-8">{children}</main>
          <footer className="text-center text-sm text-gray-400">
            &copy; 2025 Legit Security CTF. All rights reserved.
          </footer>
        </div>
      </body>
    </html>
  );
}