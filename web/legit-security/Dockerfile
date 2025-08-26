FROM oven/bun:slim AS base
WORKDIR /app

FROM base AS deps
WORKDIR /app
COPY package.json bun.lock* .npmrc* ./
RUN bun install --frozen-lockfile


FROM base AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
ENV STANDALONE=1
ENV SOMETHING_COMPLETLY_RANDOM="9b80b2ab-fde1-4ea4-b7bc-3c8f4e20847c"
ENV PECAN_TOKEN="pecan{d0nt_Bl1ndly_tru\$t_everyth1ng:(}"
RUN bun run build

FROM base AS runner
WORKDIR /app
ENV NODE_ENV=production

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

COPY --from=builder /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

USER nextjs
EXPOSE 3000
ENV PORT=3000
ENV HOSTNAME="0.0.0.0"
CMD ["bun", "server.js"]