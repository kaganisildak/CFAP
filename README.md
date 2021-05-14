# CFAP
Route applications network traffic with CloudFlare Access header over proxy


## Problem

I could not find a way for specific applications to access websites controlled by CloudFlare Access. 

Example : Github Actions Runner can't authenticate with a GHE server that's behind CloudFlare Access

## Requirements
- Cloudflared (to get access token)
- MitmProxy & CFAP plugin(for newbies)
- ProxyChain 
