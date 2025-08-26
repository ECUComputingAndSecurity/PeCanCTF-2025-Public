"use server";

export async function completePhase2Challenge({ isCompleted }: { isCompleted: boolean }, _?: any) {
  if (isCompleted) {
    const token = process.env.PECAN_TOKEN || "pecan{demo_token}";
    return { success: true, token };
  } else {
    return { success: false, message: "Are you sure you even hacked the connection?" };
  }
}