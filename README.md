# CFAP
Routing applications network traffic with CloudFlare Access header over proxy


## Problem

I could not find a way for specific applications to access websites controlled by CloudFlare Access. 

Example : Github Actions Runner can't authenticate with a GHE server that's behind CloudFlare Access

## Requirements
- [Cloudflared](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation) (to get access token)
- [MitmProxy](https://mitmproxy.org/) & CFAP plugin(for newbies)
- [ProxyChain](https://github.com/haad/proxychains) (Mac users'll disable [SIP](https://developer.apple.com/documentation/security/disabling_and_enabling_system_integrity_protection) )

# Steps
- Get Cloudflare Access Token and save to **token.conf**   
`cloudflared access login https://git.company.com`
- Modify target URL on **CFAP.py**
- Start mitmproxy with CFAP Plugin   
 `sudo ./mitmweb -s CFAP.py`
- Use proxychains with which app need access the app   
 `proxychains4 ./config.sh --url https://git.company.com/enterprises/company --token LAPSEKİLİTAYFUR`
 
 ####  Note : You can use system environments to set proxy for other apps but i couldn't route the f**** runner traffic over proxy with system environments so i created this repo to helping other fellas.
 
 ###### If there is an easier way to do this and I haven't found it in the cloudflare documentation, please let me know and let me curse myself for the time I wasted on it.
 [@kaganisildak](https://twitter.com/kaganisildak)
