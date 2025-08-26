module.exports = {
  reactStrictMode: true,
  headers: async () => [
    {
      source: '/(.*)',
      headers: [
        {
          key: 'X-Powered-By',
          value: 'Next.js 15.2.2',
        },
      ],
    },
  ],
  env: {
    SOMETHING_COMPLETLY_RANDOM: process.env.SOMETHING_COMPLETLY_RANDOM || crypto.randomUUID(),
    PECAN_TOKEN: process.env.PECAN_TOKEN || 'pecan{demo_token}',
  },
  output: process.env.STANDALONE ? 'standalone' : undefined,
} as import('next').NextConfig;