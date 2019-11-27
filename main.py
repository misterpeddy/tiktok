from client import TikTokClient

tiktok = TikTokClient()
trending = tiktok.getTrending()
print(trending)
