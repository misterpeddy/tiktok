## Components

* Client
  * Exposes REST-ful endpoints for interacting with content owned by Tiktok services
  * Uses a Browser object internally to interact with TikTok's frontend
  * When agents land, it will need to offer generator APIs for interacting with endless streams of content
* Browser
  * Orchestrates standing up Browsermob proxy and pointing a Chrome Driver to it
  * Aims to expose an interface analogous to that of Chrome for a human user
  * When agents land, it will need to have a higher level of abstraction (ex: "Get list of videos on page")
