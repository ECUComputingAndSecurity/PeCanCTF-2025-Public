"use client";

import React from "react";
import { completePhase2Challenge } from "./action";

export default function Phase2Client() {
  const handleChallengeCompletion = async (e: React.FormEvent) => {
    e.preventDefault();
    const res = await completePhase2Challenge({ isCompleted: false });
    if (!res.success) {
      alert(res.message || "Challenge not completed.");
      return;
    }
    const { token } = res;
    alert(`Challenge completed! Your token is: ${token}`);
  };

  return (
    <button
      className="bg-gradient-to-r from-purple-600 to-blue-600 hover:from-blue-700 hover:to-purple-700 text-white font-bold py-3 px-8 rounded-lg shadow-lg transition-all duration-200 text-xl opacity-60 cursor-not-allowed disabled:opacity-60 disabled:cursor-not-allowed"
      onClick={handleChallengeCompletion}
      type="submit"
    >
      Download the whole internet!
    </button>
  );
}