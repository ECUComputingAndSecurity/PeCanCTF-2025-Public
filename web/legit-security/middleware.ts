import { NextResponse, NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  const url = new URL(request.url);

  // do the bypass in that case (in theory nextjs shouldnt get here, but I can't be bothered to work out why its but so simple)
  if (request.headers.has('x-middleware-subrequest') || request.cookies.get('hmm') === process.env.SOMETHING_COMPLETLY_RANDOM) {
    const resp = NextResponse.next({});
    // @ts-ignore i give up
    resp.cookies.set('hmm', process.env.SOMETHING_COMPLETLY_RANDOM, { path: '/', expires: new Date(Date.now() + 1000 * 60 * 60 * 24 * 7) });
    return resp;
  }

  url.pathname = "/admin";
  url.search = "?lol-imagine-thinking-you-can-access-admin=" + new Date().getTime();
  return Response.redirect(url)
}

export const config = {
  matcher: ['/admin'],
};