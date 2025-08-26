import React from 'react';
import Link from 'next/link';

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen py-12 bg-gradient-to-br from-gray-950 via-purple-950 to-blue-950 dark:from-gray-900 dark:via-purple-900 dark:to-blue-900 rounded-md">
      <div className="bg-white/10 dark:bg-gray-900/70 backdrop-blur-md rounded-2xl shadow-2xl p-10 max-w-2xl w-full text-center border border-purple-700 dark:border-purple-800">
        <h2 className="text-5xl font-extrabold mb-4 text-purple-200 dark:text-purple-300 drop-shadow">Legit Security Portal</h2>
        <p className="mb-6 text-lg text-gray-100 dark:text-gray-200">
          Welcome to the Legit Security Portal, your one-stop hub for secure admin operations and knowledge. Explore our features and discover how we keep your data safe with cutting-edge middleware technology.
        </p>
        <div className="flex flex-col gap-4 items-center">
          <a href="/admin" className="bg-gradient-to-r from-purple-600 to-blue-600 hover:from-blue-700 hover:to-purple-700 text-white font-bold py-3 px-8 rounded-lg shadow-lg transition-all duration-200 text-xl">Admin Dashboard</a>
          <a href="/useless" className="bg-gradient-to-r from-gray-700 to-gray-900 hover:from-gray-800 hover:to-black text-gray-200 font-bold py-3 px-8 rounded-lg shadow-lg transition-all duration-200 text-lg">Knowledge Base</a>
        </div>
        <div className="mt-8 text-sm text-gray-300 dark:text-gray-400">
          <p>
            <span className="font-bold text-purple-300 dark:text-purple-200">Why Legit Security?</span> We use advanced middleware methods to protect sensitive areas. Security is our top priority!
          </p>
        </div>
      </div>
    </div>
  );
};
