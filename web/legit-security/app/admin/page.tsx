import Phase2Client from './page.client';

export default async function Phase2Page() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gradient-to-br from-blue-950 via-purple-950 to-gray-950 dark:from-blue-900 dark:via-purple-900 dark:to-black text-white">
      <div className="bg-white/10 dark:bg-gray-900/70 backdrop-blur-md rounded-2xl shadow-2xl p-10 max-w-lg w-full text-center border border-purple-700 dark:border-purple-800">
        <h1 className="text-4xl font-extrabold mb-4 text-purple-300 dark:text-purple-200 drop-shadow">Phase 2: Final Verification</h1>
        <p className="mb-6 text-lg text-gray-200 dark:text-gray-300">
          Welcome to the <span className="font-semibold text-purple-400 dark:text-purple-300">final phase</span> of the Legit Security Portal!
        </p>
        <p className="mb-8 text-gray-300 dark:text-gray-400">
          You have proven your skills by bypassing the <span className="font-mono text-yellow-300">/admin</span> middleware.<br />
          To claim your reward, click the button below using the 100% safe server actions!
        </p>
        <Phase2Client />
      </div>
      <div className="mt-8 text-center">
        <p className="text-xs text-gray-500 dark:text-gray-600">VERY SECRET URL, DO NOT SHARE:</p>
        <code className="text-yellow-300 font-mono text-sm bg-black/40 px-2 py-1 rounded-md select-all">
          <span>{`/admin/${process.env.SOMETHING_COMPLETLY_RANDOM}`}</span>
        </code>
      </div>
    </div>
  );
}